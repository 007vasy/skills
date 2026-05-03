#!/usr/bin/env python3
"""Residuality run-state I/O.

Subcommands:
  init       Create an empty state at --path with the given --project and --mode.
  load       Read state from --path, validate, print to stdout.
  save       Read JSON from --in (or stdin), validate, write atomically to --path.
             Always appends a history entry; never replaces prior attractors_residues.
  validate   Validate JSON at --in (or stdin) against the schema; exit non-zero on error.

Standard library only. Validation uses `jsonschema` if installed (full Draft 2020-12),
otherwise falls back to a focused minimal validator that enforces required keys, ID
patterns, enum membership, and the load-bearing minItems constraints.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path

SCHEMA_VERSION = "1.0"
SCRIPTS_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPTS_DIR.parent
SCHEMA_PATH = SKILL_ROOT / "assets" / "state_schema.json"

VALID_MODES = ("analyze", "wizard", "iterate", "contagion-only")
VALID_FOCUS = ("security", "cost", "regulatory", "performance", "safety")
VALID_REGIMES = ("frozen", "edge", "chaotic")
VALID_CATEGORIES = (
    "regulatory", "market", "tech", "human", "adversarial",
    "environmental", "supply-chain", "scale", "time",
)
VALID_KINDS = ("service", "datastore", "queue", "client", "external", "human", "device", "edge")
VALID_EDGE_KINDS = ("sync", "async", "data", "human", "device")


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def best_effort_git_sha() -> str | None:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=str(Path.cwd()),
            capture_output=True,
            text=True,
            timeout=2,
        )
        if out.returncode == 0 and out.stdout.strip():
            return out.stdout.strip()
    except Exception:
        pass
    return None


# ---------- validation ----------

def _validate_with_jsonschema(state: dict) -> list[str]:
    try:
        import jsonschema
    except ModuleNotFoundError:
        return _validate_minimal(state)
    schema = json.loads(SCHEMA_PATH.read_text())
    errors: list[str] = []
    validator = jsonschema.Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(state), key=lambda e: list(e.absolute_path)):
        path = "/".join(str(p) for p in err.absolute_path) or "<root>"
        errors.append(f"{path}: {err.message}")
    return errors


def _validate_minimal(state: dict) -> list[str]:
    """Stdlib fallback. Checks the load-bearing constraints only."""
    errs: list[str] = []
    required = ["schema_version", "project", "created_at", "updated_at", "mode",
                "naive_architecture", "user_stack_facts", "stressors",
                "attractors_residues", "residue_stack", "history"]
    for k in required:
        if k not in state:
            errs.append(f"<root>: missing required key '{k}'")
    if state.get("schema_version") != SCHEMA_VERSION:
        errs.append(f"schema_version: expected '{SCHEMA_VERSION}', got {state.get('schema_version')!r}")
    if state.get("mode") not in VALID_MODES:
        errs.append(f"mode: must be one of {VALID_MODES}")
    for f in state.get("focus", []) or []:
        if f not in VALID_FOCUS:
            errs.append(f"focus: invalid value {f!r}")
    arch = state.get("naive_architecture", {}) or {}
    if not arch.get("summary"):
        errs.append("naive_architecture.summary: must be non-empty")
    for i, c in enumerate(arch.get("components", []) or []):
        if not re.match(r"^C\d{2,}$", c.get("id", "")):
            errs.append(f"naive_architecture.components[{i}].id: must match ^C\\d{{2,}}$")
        if c.get("kind") not in VALID_KINDS:
            errs.append(f"naive_architecture.components[{i}].kind: invalid")
    for i, e in enumerate(arch.get("edges", []) or []):
        if e.get("kind") not in VALID_EDGE_KINDS:
            errs.append(f"naive_architecture.edges[{i}].kind: invalid")
    for i, s in enumerate(state.get("stressors", []) or []):
        if not re.match(r"^S\d{2,}$", s.get("id", "")):
            errs.append(f"stressors[{i}].id: must match ^S\\d{{2,}}$")
        if s.get("category") not in VALID_CATEGORIES:
            errs.append(f"stressors[{i}].category: invalid")
        if not (1 <= int(s.get("novelty", 0)) <= 5):
            errs.append(f"stressors[{i}].novelty: must be 1..5")
    for i, ar in enumerate(state.get("attractors_residues", []) or []):
        r = ar.get("residue", {})
        _validate_residue_minimal(r, f"attractors_residues[{i}].residue", errs)
    for i, r in enumerate(state.get("residue_stack", []) or []):
        _validate_residue_minimal(r, f"residue_stack[{i}]", errs)
    crit = state.get("criticality")
    if crit is not None:
        if crit.get("regime") not in VALID_REGIMES and not str(crit.get("regime", "")).startswith("indeterminate"):
            errs.append("criticality.regime: must be frozen|edge|chaotic|indeterminate ...")
    return errs


def _validate_residue_minimal(r: dict, prefix: str, errs: list[str]) -> None:
    if not re.match(r"^R\d{2,}$", r.get("id", "")):
        errs.append(f"{prefix}.id: must match ^R\\d{{2,}}$")
    if not r.get("name"):
        errs.append(f"{prefix}.name: must be non-empty")
    if not r.get("intent"):
        errs.append(f"{prefix}.intent: must be non-empty")
    if not r.get("minimal_change_description"):
        errs.append(f"{prefix}.minimal_change_description: must be non-empty")
    if not r.get("applies_to_stressors"):
        errs.append(f"{prefix}.applies_to_stressors: must have minItems 1 (theatre-residue guard)")
    if not r.get("stack_fit_citations"):
        errs.append(f"{prefix}.stack_fit_citations: must have minItems 1 (fictional-stack guard)")


def validate_state(state: dict) -> list[str]:
    return _validate_with_jsonschema(state)


# ---------- I/O ----------

def empty_state(project: str, mode: str) -> dict:
    ts = now_iso()
    return {
        "schema_version": SCHEMA_VERSION,
        "project": project,
        "created_at": ts,
        "updated_at": ts,
        "git_sha": best_effort_git_sha(),
        "mode": mode,
        "focus": [],
        "naive_architecture": {
            "summary": "<to fill in>",
            "business_context": "",
            "components": [],
            "edges": [],
            "assumptions": [],
        },
        "user_stack_facts": [],
        "stressors": [],
        "attractors_residues": [],
        "residue_stack": [],
        "history": [
            {
                "timestamp": ts,
                "mode": mode,
                "note": "init",
                "changed_sections": [],
            }
        ],
        "open_questions": [],
    }


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(payload)
        os.replace(tmp, str(path))
    except Exception:
        try:
            os.unlink(tmp)
        except FileNotFoundError:
            pass
        raise


def read_json(in_arg: str | None) -> dict:
    if in_arg and in_arg != "-":
        return json.loads(Path(in_arg).read_text(encoding="utf-8"))
    return json.loads(sys.stdin.read())


def write_json(out_arg: str | None, payload: dict) -> None:
    text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if out_arg and out_arg != "-":
        atomic_write(Path(out_arg), text)
    else:
        sys.stdout.write(text)


# ---------- subcommands ----------

def cmd_init(args: argparse.Namespace) -> int:
    state = empty_state(project=args.project, mode=args.mode)
    errs = validate_state(state)
    if errs:
        print("VALIDATION FAILED on freshly initialised state — schema bug?", file=sys.stderr)
        for e in errs:
            print("  - " + e, file=sys.stderr)
        return 2
    write_json(args.path, state)
    if args.path and args.path != "-":
        print(f"initialised: {args.path}", file=sys.stderr)
    return 0


def cmd_load(args: argparse.Namespace) -> int:
    if not args.path or not Path(args.path).exists():
        print(f"state file not found: {args.path}", file=sys.stderr)
        return 2
    state = json.loads(Path(args.path).read_text(encoding="utf-8"))
    errs = validate_state(state)
    if errs:
        print("VALIDATION FAILED on loaded state:", file=sys.stderr)
        for e in errs:
            print("  - " + e, file=sys.stderr)
        return 2
    write_json("-", state)
    return 0


def cmd_save(args: argparse.Namespace) -> int:
    state = read_json(args.in_)
    state["updated_at"] = now_iso()
    if args.git_sha:
        state["git_sha"] = best_effort_git_sha()
    history_note = args.note or ""
    history_entry = {
        "timestamp": state["updated_at"],
        "mode": state.get("mode", "analyze"),
        "note": history_note,
        "changed_sections": list(args.changed) if args.changed else [],
    }
    state.setdefault("history", []).append(history_entry)
    errs = validate_state(state)
    if errs:
        print("VALIDATION FAILED — refusing to save:", file=sys.stderr)
        for e in errs:
            print("  - " + e, file=sys.stderr)
        return 2
    write_json(args.path, state)
    if args.path and args.path != "-":
        print(f"saved: {args.path} (history entries: {len(state['history'])})", file=sys.stderr)
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    state = read_json(args.in_)
    errs = validate_state(state)
    if errs:
        for e in errs:
            print(e)
        return 2
    print("OK")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Residuality run-state I/O")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="Initialise an empty state file")
    p_init.add_argument("--project", required=True)
    p_init.add_argument("--mode", default="analyze", choices=VALID_MODES)
    p_init.add_argument("--path", required=True, help="Path to write the new state file")
    p_init.set_defaults(func=cmd_init)

    p_load = sub.add_parser("load", help="Load and validate a state file; print to stdout")
    p_load.add_argument("--path", required=True)
    p_load.set_defaults(func=cmd_load)

    p_save = sub.add_parser("save", help="Read state JSON, validate, write atomically; appends history entry")
    p_save.add_argument("--in", dest="in_", default="-", help="Path to read state JSON from, or '-' for stdin")
    p_save.add_argument("--path", required=True, help="Path to write the updated state file")
    p_save.add_argument("--note", default="", help="One-line note for the history entry")
    p_save.add_argument("--changed", nargs="*", default=None, help="changed_sections list for the history entry")
    p_save.add_argument("--git-sha", action="store_true", help="Refresh git_sha at save time")
    p_save.set_defaults(func=cmd_save)

    p_val = sub.add_parser("validate", help="Validate state JSON; exit non-zero on error")
    p_val.add_argument("--in", dest="in_", default="-", help="Path to read state JSON from, or '-' for stdin")
    p_val.set_defaults(func=cmd_validate)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
