#!/usr/bin/env python3
"""Residue dedupe.

Reads a residuality state JSON. Collects every residue from
`attractors_residues[].residue` (and any pre-existing `residue_stack[]`),
fuzzy-merges near-duplicates, and writes the deduped list back into
`residue_stack[]`. The `attractors_residues` array is left untouched (it is
the per-stressor history of derivation).

Merge rule (matches references/prompt_templates.md Block E):
- Compute name similarity (Levenshtein-based ratio on normalised names).
- Compute intent similarity (Jaccard on intent token sets).
- combined_similarity = (name_sim + intent_sim) / 2
- Merge two residues if combined_similarity >= --merge-threshold (default 0.75)
  OR if both have the same non-null source_pattern AND combined_similarity >= --pattern-threshold (default 0.55).

The merged residue keeps:
- The id and name of the kept residue (the one with more applies_to_stressors,
  ties broken by smaller numeric id).
- The union of applies_to_stressors and stack_fit_citations from the pair.
- A merge_log entry recording {kept_id, dropped_id, similarity}.

Use `--keep-both ID1 ID2` (repeatable) to force a pair to NOT merge — useful for
the marginal band 0.55-0.85 where a human reviewer disagrees with the score.

Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

STOPWORDS = {
    "a", "an", "the", "and", "or", "of", "to", "for", "with", "on", "in", "by",
    "at", "as", "is", "be", "has", "have", "this", "that", "from", "via", "per",
    "into", "no", "not", "any", "all", "some", "we", "our",
}

DEFAULT_MERGE_THRESHOLD = 0.75
DEFAULT_PATTERN_THRESHOLD = 0.55


def normalise(text: str) -> list[str]:
    text = (text or "").lower()
    tokens = re.findall(r"[a-z0-9]+", text)
    return [t for t in tokens if t not in STOPWORDS and len(t) > 1]


def jaccard(a: list[str], b: list[str]) -> float:
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def levenshtein(a: str, b: str) -> int:
    if a == b:
        return 0
    if len(a) < len(b):
        a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, start=1):
        curr = [i] + [0] * len(b)
        for j, cb in enumerate(b, start=1):
            ins = curr[j - 1] + 1
            dele = prev[j] + 1
            sub = prev[j - 1] + (0 if ca == cb else 1)
            curr[j] = min(ins, dele, sub)
        prev = curr
    return prev[-1]


def name_ratio(a: str, b: str) -> float:
    """1 - normalised Levenshtein distance over normalised name tokens (joined)."""
    aa = " ".join(normalise(a))
    bb = " ".join(normalise(b))
    if not aa and not bb:
        return 0.0
    if aa == bb:
        return 1.0
    dist = levenshtein(aa, bb)
    return 1.0 - dist / max(len(aa), len(bb))


def collect_input_residues(state: dict) -> list[dict]:
    seen: dict[str, dict] = {}
    for ar in state.get("attractors_residues") or []:
        r = ar.get("residue")
        if r and "id" in r:
            seen.setdefault(r["id"], r)
    for r in state.get("residue_stack") or []:
        if r and "id" in r:
            seen.setdefault(r["id"], r)
    return list(seen.values())


def kept_first(a: dict, b: dict) -> tuple[dict, dict]:
    """Return (keep, drop) — keep is whichever has more applies_to_stressors,
    ties broken by lower numeric id."""
    a_n = len(a.get("applies_to_stressors") or [])
    b_n = len(b.get("applies_to_stressors") or [])
    if a_n != b_n:
        return (a, b) if a_n > b_n else (b, a)
    a_id = int(re.sub(r"[^0-9]", "", a.get("id", "0")) or 0)
    b_id = int(re.sub(r"[^0-9]", "", b.get("id", "0")) or 0)
    return (a, b) if a_id <= b_id else (b, a)


def merge_pair(keep: dict, drop: dict, similarity: float) -> dict:
    keep = dict(keep)
    keep["applies_to_stressors"] = sorted(set((keep.get("applies_to_stressors") or [])
                                              + (drop.get("applies_to_stressors") or [])))
    keep["stack_fit_citations"] = sorted(set((keep.get("stack_fit_citations") or [])
                                             + (drop.get("stack_fit_citations") or [])))
    log = list(keep.get("merge_log") or [])
    log.append({
        "kept_id": keep["id"],
        "dropped_id": drop["id"],
        "similarity": round(similarity, 3),
    })
    keep["merge_log"] = log
    if not keep.get("source_pattern") and drop.get("source_pattern"):
        keep["source_pattern"] = drop["source_pattern"]
    return keep


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Dedupe residues into residue_stack")
    p.add_argument("--in", dest="in_", default="-", help="path to state.json or '-'")
    p.add_argument("--out", default="-", help="path to write updated state.json or '-'")
    p.add_argument("--merge-threshold", type=float, default=DEFAULT_MERGE_THRESHOLD)
    p.add_argument("--pattern-threshold", type=float, default=DEFAULT_PATTERN_THRESHOLD)
    p.add_argument("--keep-both", nargs=2, action="append", default=[],
                   metavar=("ID1", "ID2"),
                   help="force this pair to NOT merge (repeatable)")
    p.add_argument("--report-only", action="store_true",
                   help="print merge plan to stderr, do not modify state")
    args = p.parse_args(argv)

    if args.in_ and args.in_ != "-":
        state = json.loads(Path(args.in_).read_text(encoding="utf-8"))
    else:
        state = json.loads(sys.stdin.read())

    keep_both = {tuple(sorted(pair)) for pair in args.keep_both}

    residues = collect_input_residues(state)
    if not residues:
        print("no residues to dedupe; residue_stack will be empty", file=sys.stderr)
        state["residue_stack"] = []
        if args.out == "-":
            sys.stdout.write(json.dumps(state, indent=2) + "\n")
        else:
            Path(args.out).write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
        return 0

    # Sort for stable comparison order: by id ascending
    residues.sort(key=lambda r: r.get("id", ""))

    merged: list[dict] = []
    for r in residues:
        absorbed = False
        for i, existing in enumerate(merged):
            pair = tuple(sorted([existing.get("id", ""), r.get("id", "")]))
            if pair in keep_both:
                continue
            n_sim = name_ratio(existing.get("name", ""), r.get("name", ""))
            i_sim = jaccard(normalise(existing.get("intent", "")),
                            normalise(r.get("intent", "")))
            combined = (n_sim + i_sim) / 2.0
            same_pattern = (
                existing.get("source_pattern")
                and r.get("source_pattern")
                and existing["source_pattern"] == r["source_pattern"]
            )
            should_merge = (combined >= args.merge_threshold) or (
                same_pattern and combined >= args.pattern_threshold
            )
            if should_merge:
                keep, drop = kept_first(existing, r)
                merged[i] = merge_pair(keep, drop, combined)
                absorbed = True
                break
        if not absorbed:
            new_entry = dict(r)
            # initialise an empty merge_log if absent so the schema field is consistent
            new_entry.setdefault("merge_log", [])
            merged.append(new_entry)

    if args.report_only:
        for r in merged:
            if r.get("merge_log"):
                for log in r["merge_log"]:
                    print(f"merged {log['dropped_id']} -> {log['kept_id']} (sim={log['similarity']})", file=sys.stderr)
        print(f"residue_stack would have {len(merged)} entries (input: {len(residues)})", file=sys.stderr)
        return 0

    state["residue_stack"] = merged
    text = json.dumps(state, indent=2) + "\n"
    if args.out == "-":
        sys.stdout.write(text)
    else:
        Path(args.out).write_text(text, encoding="utf-8")
    print(f"residue_stack: {len(merged)} (input: {len(residues)})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
