#!/usr/bin/env python3
"""Render a happy_paths/<slug>.md file as a Playwright spec (.spec.ts).

Pipeline:
  parse_happy_path.py --in happy_paths/<slug>.md  →  this script  →  .spec.ts

Output goes to stdout or to <out>/happy-paths/<slug>.spec.ts when --out is a dir.

Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Map parsed action -> Playwright code emitter.

PLACEHOLDER_RE = re.compile(r"\{\{[^}]+\}\}")

INDENT = "  "


def _ts_string(s: str) -> str:
    """Emit a TypeScript string literal. If it contains {{...}}, wrap in subst()."""
    if s is None:
        return '""'
    escaped = s.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")
    if PLACEHOLDER_RE.search(s):
        return f"subst(`{escaped}`, runtime)"
    return f"`{escaped}`"


def _selector_literal(sel: str | None) -> str:
    if not sel:
        return '""'
    return _ts_string(sel)


def _comment(step: dict[str, Any]) -> str:
    return f"{INDENT}// step {step['n']}: {step['raw']}"


def emit_step(step: dict[str, Any]) -> list[str]:
    a = step["action"]
    out: list[str] = [_comment(step)]
    sel = step.get("selector")
    expect = step.get("expect")

    if a == "navigate":
        target = step.get("target") or "/"
        if target.startswith("http://") or target.startswith("https://"):
            out.append(f"{INDENT}await page.goto({_ts_string(target)});")
        elif PLACEHOLDER_RE.search(target):
            out.append(f"{INDENT}await page.goto(BASE_URL + {_ts_string(target)});")
        else:
            esc = target.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")
            out.append(f"{INDENT}await page.goto(`${{BASE_URL}}{esc}`);")
    elif a == "click":
        out.append(f"{INDENT}await selectorToLocator(page, {_selector_literal(sel)}).click();")
    elif a == "fill":
        val = step.get("value") or ""
        out.append(f"{INDENT}await selectorToLocator(page, {_selector_literal(sel)}).fill({_ts_string(val)});")
    elif a == "select":
        val = step.get("value") or ""
        out.append(f"{INDENT}await selectorToLocator(page, {_selector_literal(sel)}).selectOption({_ts_string(val)});")
    elif a == "check":
        out.append(f"{INDENT}await selectorToLocator(page, {_selector_literal(sel)}).check();")
    elif a == "uncheck":
        out.append(f"{INDENT}await selectorToLocator(page, {_selector_literal(sel)}).uncheck();")
    elif a == "upload":
        val = step.get("value") or ""
        out.append(
            f"{INDENT}await selectorToLocator(page, {_selector_literal(sel)}).setInputFiles({_ts_string(val)});"
        )
    elif a == "press":
        val = step.get("value") or "Enter"
        out.append(f"{INDENT}await page.keyboard.press({_ts_string(val)});")
    elif a == "wait_for":
        target = step.get("target") or ""
        # Recognise common shapes: "selector X", "url contains X", "network idle"
        low = target.lower()
        if low.startswith("url contains "):
            frag = target[len("url contains ") :].strip().strip("`")
            out.append(f"{INDENT}await page.waitForURL(new RegExp({json.dumps(re.escape(frag))}));")
        elif low.startswith("selector "):
            csel = target[len("selector ") :].strip().strip("`")
            out.append(
                f"{INDENT}await selectorToLocator(page, {_ts_string(csel)}).waitFor({{ state: 'visible' }});"
            )
        elif "network idle" in low:
            out.append(f"{INDENT}await page.waitForLoadState('networkidle');")
        elif sel:
            out.append(
                f"{INDENT}await selectorToLocator(page, {_selector_literal(sel)}).waitFor({{ state: 'visible' }});"
            )
        else:
            out.append(f"{INDENT}// TODO: unrecognised wait target — {target!r}")
    elif a == "assert":
        if sel:
            if expect and "contains" in expect.lower():
                m = re.search(r"contains\s+(.+)$", expect, re.IGNORECASE)
                needle = m.group(1).strip().strip("`").strip('"').strip("'") if m else expect
                out.append(
                    f"{INDENT}await expect(selectorToLocator(page, {_selector_literal(sel)})).toContainText({_ts_string(needle)});"
                )
            elif expect and "visible" in expect.lower():
                out.append(
                    f"{INDENT}await expect(selectorToLocator(page, {_selector_literal(sel)})).toBeVisible();"
                )
            else:
                out.append(
                    f"{INDENT}await expect(selectorToLocator(page, {_selector_literal(sel)})).toBeVisible();"
                )
        elif expect:
            # URL assertion
            m = re.search(r"url\s+(?:contains|matches)\s+(.+)$", expect, re.IGNORECASE)
            if m:
                frag = m.group(1).strip().strip("`")
                out.append(f"{INDENT}await expect(page).toHaveURL(new RegExp({json.dumps(re.escape(frag))}));")
            else:
                out.append(f"{INDENT}// TODO: assertion without selector — {expect!r}")
    else:
        out.append(f"{INDENT}// TODO: unknown action {a!r}")

    # Handle inline expect on action-bearing verbs (e.g. Click ... Expect: navigation to URL)
    if a not in ("assert",) and expect:
        low = expect.lower()
        m = re.search(r"url\s+(?:contains|containing)\s+(.+)$", low)
        if m:
            frag = expect[m.start(1):].strip().strip("`").rstrip(".")
            out.append(f"{INDENT}await expect(page).toHaveURL(new RegExp({json.dumps(re.escape(frag))}));")
        elif "visible" in low and sel:
            out.append(
                f"{INDENT}await expect(selectorToLocator(page, {_selector_literal(sel)})).toBeVisible();"
            )

    return out


def render(parsed: dict[str, Any], source_path: str) -> str:
    fm = parsed.get("frontmatter") or {}
    steps = parsed.get("steps") or []
    slug = fm.get("slug", "unknown")
    title = fm.get("title", slug)
    base_url = ((fm.get("runner_hints") or {}).get("base_url")) or ""
    test_data = fm.get("test_data") or {}

    tmpl_path = Path(__file__).parent.parent / "assets" / "playwright_test.tmpl"
    tmpl = tmpl_path.read_text(encoding="utf-8")

    steps_block = "\n".join(line for s in steps for line in emit_step(s))

    out = (
        tmpl.replace("{{slug}}", slug)
        .replace("{{title}}", title.replace("`", "\\`"))
        .replace("{{source_path}}", source_path)
        .replace("{{generated_at}}", datetime.now(timezone.utc).isoformat(timespec="seconds"))
        .replace("{{base_url_literal}}", json.dumps(base_url))
        .replace("{{test_data_literal}}", json.dumps(test_data, indent=2))
        .replace("{{steps_block}}", steps_block)
    )
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Render parsed happy path as a Playwright spec")
    p.add_argument("--in", dest="in_", default="-", help="parsed JSON path or '-'")
    p.add_argument("--source", default="happy_paths/<slug>.md", help="source .md path for the header comment")
    p.add_argument("--out", default="-", help="path to .spec.ts or '-'")
    args = p.parse_args(argv)

    if args.in_ == "-":
        text = sys.stdin.read()
    else:
        text = Path(args.in_).read_text(encoding="utf-8")
    parsed = json.loads(text)

    rendered = render(parsed, args.source)
    if args.out == "-":
        sys.stdout.write(rendered)
    else:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(rendered, encoding="utf-8")
    print(f"rendered: {len(parsed.get('steps') or [])} steps -> Playwright spec", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
