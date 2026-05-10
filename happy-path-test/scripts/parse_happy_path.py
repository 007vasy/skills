#!/usr/bin/env python3
"""Parse a happy_paths/<slug>.md file into structured JSON.

Output shape:
  {
    "frontmatter": { ... },          # parsed YAML-lite frontmatter
    "steps": [                       # one entry per numbered step in ## Steps
      { "n": int, "verb": str, "action": str, "target": str,
        "selector": str|null, "expect": str|null, "value": str|null,
        "note": str|null, "raw": str }
    ],
    "warnings": [ str, ... ]         # spec-violation warnings (non-fatal)
  }

The format accepted is defined by ../happy-paths/references/format_spec.md.

Stdlib only — no PyYAML, no markdown lib. The YAML subset is intentionally
narrow (matches the spec exactly): top-level scalars, inline lists, inline
maps, and one level of nested map/list blocks under a "key:" line.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

# ---------- YAML-lite ------------------------------------------------------

_INLINE_LIST = re.compile(r"^\[(.*)\]$")
_INLINE_MAP = re.compile(r"^\{(.*)\}$")


def _strip_comment(s: str) -> str:
    in_str: str | None = None
    out: list[str] = []
    for i, ch in enumerate(s):
        if in_str:
            out.append(ch)
            if ch == in_str and (i == 0 or s[i - 1] != "\\"):
                in_str = None
            continue
        if ch in ('"', "'"):
            in_str = ch
            out.append(ch)
            continue
        if ch == "#":
            break
        out.append(ch)
    return "".join(out).rstrip()


def _coerce_scalar(s: str) -> Any:
    s = s.strip()
    if s == "":
        return None
    low = s.lower()
    if low in ("null", "~"):
        return None
    if low == "true":
        return True
    if low == "false":
        return False
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    if re.fullmatch(r"-?\d+\.\d+", s):
        return float(s)
    return s


def _parse_inline(s: str) -> Any:
    s = s.strip()
    m = _INLINE_LIST.match(s)
    if m:
        body = m.group(1).strip()
        if not body:
            return []
        return [_coerce_scalar(x) for x in _split_top_commas(body)]
    m = _INLINE_MAP.match(s)
    if m:
        body = m.group(1).strip()
        if not body:
            return {}
        out: dict[str, Any] = {}
        for part in _split_top_commas(body):
            if ":" not in part:
                continue
            k, v = part.split(":", 1)
            out[k.strip()] = _coerce_scalar(v.strip())
        return out
    return _coerce_scalar(s)


def _split_top_commas(s: str) -> list[str]:
    parts: list[str] = []
    depth = 0
    in_str: str | None = None
    cur: list[str] = []
    for ch in s:
        if in_str:
            cur.append(ch)
            if ch == in_str:
                in_str = None
            continue
        if ch in ('"', "'"):
            in_str = ch
            cur.append(ch)
            continue
        if ch in "[{":
            depth += 1
            cur.append(ch)
            continue
        if ch in "]}":
            depth -= 1
            cur.append(ch)
            continue
        if ch == "," and depth == 0:
            parts.append("".join(cur))
            cur = []
            continue
        cur.append(ch)
    if cur:
        parts.append("".join(cur))
    return parts


def parse_yaml_lite(text: str) -> dict[str, Any]:
    """Parse the narrow YAML subset used by happy-path frontmatter."""
    lines = [_strip_comment(l).rstrip() for l in text.split("\n")]
    result: dict[str, Any] = {}
    n = len(lines)
    i = 0
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith(" "):
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        k, v = line.split(":", 1)
        key = k.strip()
        value_str = v.strip()
        if value_str:
            result[key] = _parse_inline(value_str)
            i += 1
            continue
        # Block follows — find first non-blank indented line
        j = i + 1
        while j < n and lines[j].strip() == "":
            j += 1
        if j >= n or not lines[j].startswith(" "):
            result[key] = None
            i = j
            continue
        child = lines[j].lstrip()
        if child.startswith("- "):
            items: list[Any] = []
            while j < n and (lines[j].startswith(" ") or lines[j].strip() == ""):
                if lines[j].strip() == "":
                    j += 1
                    continue
                stripped = lines[j].lstrip()
                if not stripped.startswith("- "):
                    break
                items.append(_parse_inline(stripped[2:].strip()))
                j += 1
            result[key] = items
            i = j
        else:
            submap: dict[str, Any] = {}
            while j < n and (lines[j].startswith(" ") or lines[j].strip() == ""):
                if lines[j].strip() == "":
                    j += 1
                    continue
                stripped = lines[j].lstrip()
                if ":" not in stripped:
                    break
                sk, sv = stripped.split(":", 1)
                submap[sk.strip()] = _parse_inline(sv.strip())
                j += 1
            result[key] = submap
            i = j
    return result


# ---------- Step parser ----------------------------------------------------

_STEP_RE = re.compile(r"^\s*(\d+)\.\s+\*\*([^*]+)\*\*\s*(.*)$")
_SUB_RE = re.compile(
    r"^\s+-\s+(Selector|Expect|Verify|Assert|Note)\s*:\s*(.*)$",
    re.IGNORECASE,
)

VERB_MAP = {
    "navigate to": "navigate",
    "click": "click",
    "fill": "fill",
    "select": "select",
    "check": "check",
    "uncheck": "uncheck",
    "upload": "upload",
    "press": "press",
    "wait for": "wait_for",
    "expect": "assert",
    "verify": "assert",
    "assert": "assert",
}

ACTIONS_NEEDING_SELECTOR = {"click", "fill", "select", "check", "uncheck", "upload"}


def _strip_backticks(s: str) -> str:
    s = s.strip()
    if s.startswith("`") and s.endswith("`") and len(s) >= 2:
        return s[1:-1]
    return s


def parse_steps(body: str) -> tuple[list[dict], list[str]]:
    warnings: list[str] = []
    m = re.search(r"^##\s+Steps\s*$", body, re.MULTILINE)
    if not m:
        warnings.append("No '## Steps' section found")
        return [], warnings
    after = body[m.end():]
    nxt = re.search(r"^##\s+", after, re.MULTILINE)
    section = after if not nxt else after[: nxt.start()]

    steps: list[dict] = []
    current: dict | None = None

    for line in section.split("\n"):
        sm = _STEP_RE.match(line)
        if sm:
            if current is not None:
                steps.append(current)
            n_ = int(sm.group(1))
            verb_raw = sm.group(2).strip()
            target_raw = sm.group(3).strip()
            verb_norm = re.sub(r"\s+", " ", verb_raw).lower()
            action = VERB_MAP.get(verb_norm)
            if action is None:
                warnings.append(f"Step {n_}: unknown verb {verb_raw!r}")
                action = verb_norm
            current = {
                "n": n_,
                "raw": line.strip(),
                "verb": verb_raw,
                "action": action,
                "target": target_raw,
                "selector": None,
                "expect": None,
                "value": None,
                "note": None,
            }
            _apply_verb_extraction(current)
            continue
        sub = _SUB_RE.match(line)
        if sub and current is not None:
            kind = sub.group(1).lower()
            value = sub.group(2).strip()
            if kind == "selector":
                current["selector"] = _strip_backticks(value)
            elif kind in ("expect", "verify", "assert"):
                # Sub-bullet always wins over the inline assert-verb description.
                if current["action"] == "assert" and current["expect"] and current["target"] == "":
                    # Inline description was stashed in expect by _apply_verb_extraction;
                    # promote it to `target` so the sub-bullet's `expect` is the assertion.
                    current["target"] = current["expect"]
                    current["expect"] = value
                elif current["expect"] is None:
                    current["expect"] = value
                else:
                    current["expect"] += "; " + value
            elif kind == "note":
                current["note"] = value

    if current is not None:
        steps.append(current)

    for s in steps:
        if s["action"] in ACTIONS_NEEDING_SELECTOR and not s["selector"]:
            warnings.append(
                f"Step {s['n']}: action {s['verb']!r} has no Selector — runner will guess"
            )

    return steps, warnings


def _apply_verb_extraction(step: dict) -> None:
    action = step["action"]
    target = step["target"]

    if action == "navigate":
        step["target"] = _strip_backticks(target)
        return
    if action == "fill":
        m = re.search(r"\s+with\s+", target, re.IGNORECASE)
        if m:
            step["target"] = target[: m.start()].strip()
            step["value"] = _strip_backticks(target[m.end():].strip())
        return
    if action == "press":
        step["value"] = _strip_backticks(target)
        step["target"] = ""
        return
    if action == "select":
        if "=" in target:
            left, right = target.rsplit("=", 1)
            step["target"] = left.strip()
            step["value"] = right.strip().strip('"').strip("'")
        return
    if action == "upload":
        m = re.search(r"\s+to\s+", target, re.IGNORECASE)
        if m:
            step["value"] = target[: m.start()].strip()
            step["target"] = target[m.end():].strip()
        return
    if action == "assert":
        step["expect"] = target if target else step["expect"]
        step["target"] = ""
        return
    # click, check, uncheck, wait_for: target stays as-is


# ---------- Top-level ------------------------------------------------------

REQUIRED_FRONTMATTER = (
    "slug",
    "title",
    "user_problem",
    "persona",
    "preconditions",
    "test_data",
    "success_criteria",
    "out_of_scope",
)


def parse_file(text: str) -> dict:
    warnings: list[str] = []
    if not text.startswith("---"):
        warnings.append("File does not start with '---' frontmatter fence")
        return {"frontmatter": {}, "steps": [], "warnings": warnings}
    end = text.find("\n---", 3)
    if end < 0:
        warnings.append("Frontmatter not closed by '---'")
        return {"frontmatter": {}, "steps": [], "warnings": warnings}
    fm_text = text[3:end].strip("\n")
    body = text[end + 4 :].lstrip("\n")

    fm = parse_yaml_lite(fm_text)
    for r in REQUIRED_FRONTMATTER:
        if r not in fm:
            warnings.append(f"Frontmatter missing required key: {r}")

    if "slug" in fm and isinstance(fm["slug"], str):
        if not re.fullmatch(r"[a-z0-9-]{1,40}", fm["slug"]):
            warnings.append(
                f"Slug {fm['slug']!r} violates [a-z0-9-]{{1,40}} (see format_spec.md)"
            )

    steps, step_warnings = parse_steps(body)
    warnings.extend(step_warnings)

    return {"frontmatter": fm, "steps": steps, "warnings": warnings}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Parse a happy_path .md to JSON")
    p.add_argument("--in", dest="in_", default="-", help="path to .md or '-' for stdin")
    p.add_argument("--out", default="-", help="path to write JSON or '-' for stdout")
    args = p.parse_args(argv)

    if args.in_ == "-":
        text = sys.stdin.read()
    else:
        text = Path(args.in_).read_text(encoding="utf-8")

    result = parse_file(text)
    out = json.dumps(result, indent=2) + "\n"
    if args.out == "-":
        sys.stdout.write(out)
    else:
        Path(args.out).write_text(out, encoding="utf-8")
    print(
        f"parsed: {len(result['steps'])} steps, {len(result['warnings'])} warnings",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
