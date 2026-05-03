#!/usr/bin/env python3
"""Stressor diversity checker.

Reads a state JSON (or a stand-alone {stressors: [...]} JSON) and reports:
  - category_coverage:  count per category
  - missing_categories: categories below their min_count floor
  - boring_score:       0..1 — how boring this list looks (lower = more diverse)
  - novelty_average:    average novelty 1..5
  - black_swan_count:   stressors with novelty == 5
  - suggestions:        textual hints about what to add

Exits non-zero if floors fail or if boring_score exceeds the threshold defined in
assets/stressor_categories.json.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPTS_DIR.parent
CATEGORIES_PATH = SKILL_ROOT / "assets" / "stressor_categories.json"
BLACK_SWAN_FLOOR = 3


def load_categories() -> dict:
    return json.loads(CATEGORIES_PATH.read_text(encoding="utf-8"))


def read_input(in_arg: str | None) -> dict:
    if in_arg and in_arg != "-":
        return json.loads(Path(in_arg).read_text(encoding="utf-8"))
    return json.loads(sys.stdin.read())


def extract_stressors(payload: dict) -> list[dict]:
    if "stressors" in payload and isinstance(payload["stressors"], list):
        return payload["stressors"]
    raise SystemExit("input JSON must have a top-level 'stressors' array")


def boring_score(stressors: list[dict], category_coverage: dict[str, int],
                 cat_meta: dict[str, dict]) -> float:
    """0..1, where 1 is maximally boring.

    Heuristic blend:
    - half: how far the average novelty is below the floor (zero if at/above)
    - half: fraction of categories below their floor
    """
    if not stressors:
        return 1.0
    novelty_avg = sum(int(s.get("novelty", 1)) for s in stressors) / len(stressors)
    novelty_floor = float(load_categories().get("novelty_average_floor", 3.0))
    novelty_term = max(0.0, (novelty_floor - novelty_avg) / novelty_floor)
    cats_below = sum(1 for cid, meta in cat_meta.items() if category_coverage.get(cid, 0) < meta["min_count"])
    cat_term = cats_below / max(1, len(cat_meta))
    return round(0.5 * novelty_term + 0.5 * cat_term, 4)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Stressor diversity check")
    p.add_argument("--in", dest="in_", default="-", help="path to state.json or '-' for stdin")
    p.add_argument("--out", default="-", help="path to write report JSON or '-' for stdout")
    p.add_argument("--strict", action="store_true",
                   help="exit non-zero on floor failures or boring_score above threshold (default: report only)")
    args = p.parse_args(argv)

    payload = read_input(args.in_)
    stressors = extract_stressors(payload)

    cat_doc = load_categories()
    cat_meta = {c["id"]: c for c in cat_doc["categories"]}
    boring_threshold = float(cat_doc.get("boring_score_threshold", 0.6))

    coverage = {cid: 0 for cid in cat_meta.keys()}
    for s in stressors:
        cat = s.get("category")
        if cat in coverage:
            coverage[cat] += 1
        else:
            coverage.setdefault(cat or "<unknown>", 0)
            coverage[cat or "<unknown>"] += 1

    missing = [cid for cid, meta in cat_meta.items() if coverage.get(cid, 0) < meta["min_count"]]
    novelty_avg = round(sum(int(s.get("novelty", 1)) for s in stressors) / max(1, len(stressors)), 3)
    black_swan = sum(1 for s in stressors if int(s.get("novelty", 0)) == 5)
    score = boring_score(stressors, coverage, cat_meta)

    suggestions: list[str] = []
    for cid in missing:
        meta = cat_meta[cid]
        gap = meta["min_count"] - coverage.get(cid, 0)
        sample = "; ".join(meta.get("examples", [])[:2])
        suggestions.append(f"add {gap} more '{cid}' stressor(s); inspiration: {sample}")
    if novelty_avg < float(cat_doc.get("novelty_average_floor", 3.0)):
        suggestions.append(f"average novelty {novelty_avg} is below floor; add stressors with novelty 4-5")
    if black_swan < BLACK_SWAN_FLOOR:
        suggestions.append(f"only {black_swan} novelty-5 (black-swan) stressors; floor is {BLACK_SWAN_FLOOR}")
    if len(stressors) < 30:
        suggestions.append(f"only {len(stressors)} stressors; aim for 30+ for a serious analysis")

    report = {
        "stressor_count": len(stressors),
        "category_coverage": coverage,
        "missing_categories": missing,
        "boring_score": score,
        "boring_score_threshold": boring_threshold,
        "novelty_average": novelty_avg,
        "novelty_average_floor": float(cat_doc.get("novelty_average_floor", 3.0)),
        "black_swan_count": black_swan,
        "black_swan_floor": BLACK_SWAN_FLOOR,
        "suggestions": suggestions,
        "passes": (not missing) and (score <= boring_threshold) and (black_swan >= BLACK_SWAN_FLOOR),
    }

    text = json.dumps(report, indent=2) + "\n"
    if args.out and args.out != "-":
        Path(args.out).write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)

    if args.strict and not report["passes"]:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
