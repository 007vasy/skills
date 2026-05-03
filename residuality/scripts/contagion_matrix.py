#!/usr/bin/env python3
"""Contagion matrix builder.

Reads a residuality state JSON. Computes:
  - incidence:           binary matrix, rows = residue_stack, cols = stressors
  - stressor_coverage:   per-stressor count of residues addressing it / 1
  - residue_load:        per-residue count of stressors addressed
  - coupling_matrix:     residue x residue, from contagion.couplings + shared
                         applies_to_stressors heuristic
  - brittleness_rank:    top entries scored by load * average outgoing coupling
  - hotspots:            top-quartile residues by load * brittleness, max 5
  - orphan_residues:     residues with empty applies_to_stressors

Writes the result back into state.contagion. The user-supplied couplings array
in state.contagion.couplings is preserved (it is the input).

Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

SHARED_STRESSOR_BONUS = 0.15  # added to coupling per shared stressor (capped)
SHARED_STRESSOR_CAP = 0.6


def build_incidence(residues: list[dict], stressors: list[dict]) -> list[list[int]]:
    s_index = {s["id"]: i for i, s in enumerate(stressors)}
    matrix = []
    for r in residues:
        row = [0] * len(stressors)
        for sid in r.get("applies_to_stressors") or []:
            if sid in s_index:
                row[s_index[sid]] = 1
        matrix.append(row)
    return matrix


def build_coupling_matrix(residues: list[dict], couplings: list[dict]) -> list[list[float]]:
    n = len(residues)
    r_index = {r["id"]: i for i, r in enumerate(residues)}
    matrix = [[0.0] * n for _ in range(n)]

    # explicit user couplings (symmetric)
    for c in couplings:
        i = r_index.get(c.get("from_residue"))
        j = r_index.get(c.get("to_residue"))
        w = float(c.get("weight", 0.0))
        if i is None or j is None or i == j:
            continue
        matrix[i][j] = max(matrix[i][j], w)
        matrix[j][i] = max(matrix[j][i], w)

    # shared-stressor heuristic on top
    stressor_sets = [set(r.get("applies_to_stressors") or []) for r in residues]
    for i in range(n):
        for j in range(i + 1, n):
            shared = len(stressor_sets[i] & stressor_sets[j])
            if shared > 0:
                bonus = min(SHARED_STRESSOR_CAP, shared * SHARED_STRESSOR_BONUS)
                matrix[i][j] = max(matrix[i][j], bonus)
                matrix[j][i] = max(matrix[j][i], bonus)
    return matrix


def percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    sorted_vals = sorted(values)
    k = (len(sorted_vals) - 1) * (pct / 100.0)
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return sorted_vals[f]
    return sorted_vals[f] + (sorted_vals[c] - sorted_vals[f]) * (k - f)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Build contagion matrix")
    p.add_argument("--in", dest="in_", default="-", help="path to state.json or '-'")
    p.add_argument("--out", default="-", help="path to write updated state.json or '-'")
    args = p.parse_args(argv)

    if args.in_ and args.in_ != "-":
        state = json.loads(Path(args.in_).read_text(encoding="utf-8"))
    else:
        state = json.loads(sys.stdin.read())

    residues = state.get("residue_stack") or []
    stressors = state.get("stressors") or []
    contagion_in = state.get("contagion") or {}
    couplings = contagion_in.get("couplings") or []

    if not residues:
        print("residue_stack is empty; run residue_dedupe first", file=sys.stderr)
        return 2

    incidence = build_incidence(residues, stressors)
    coupling_matrix = build_coupling_matrix(residues, couplings)

    residue_load = {r["id"]: sum(row) for r, row in zip(residues, incidence)}
    if stressors:
        stressor_coverage_counts = [sum(row[j] for row in incidence) for j in range(len(stressors))]
        stressor_coverage = {
            stressors[j]["id"]: round(min(1.0, c / 1.0), 3)
            for j, c in enumerate(stressor_coverage_counts)
        }
    else:
        stressor_coverage = {}

    # brittleness: load * avg outgoing coupling
    brittleness = []
    for i, r in enumerate(residues):
        avg_coupling = sum(coupling_matrix[i]) / max(1, len(residues) - 1)
        score = round(residue_load[r["id"]] * avg_coupling, 4)
        why = ""
        if avg_coupling > 0:
            top_neighbour_idx = max(range(len(residues)), key=lambda j: coupling_matrix[i][j] if j != i else -1)
            top_neighbour = residues[top_neighbour_idx]["id"]
            why = f"load={residue_load[r['id']]}, top coupling -> {top_neighbour} ({round(coupling_matrix[i][top_neighbour_idx],2)})"
        brittleness.append({"residue_id": r["id"], "score": score, "why": why})
    brittleness.sort(key=lambda x: x["score"], reverse=True)
    brittleness_rank = brittleness[:5]

    # hotspots: top-quartile by load * brittleness score
    combined_scores = [
        (r["id"], residue_load[r["id"]] * b["score"])
        for r, b in zip(residues, brittleness)
    ]
    combined_scores_only = [s for _, s in combined_scores if s > 0]
    threshold = percentile(combined_scores_only, 75) if combined_scores_only else 0
    hotspots = []
    for rid, score in combined_scores:
        if score >= threshold and score > 0:
            hotspots.append({
                "residue_id": rid,
                "reason": f"load*brittleness={round(score,3)} >= 75th percentile ({round(threshold,3)})"
            })
    hotspots.sort(key=lambda h: h["reason"], reverse=True)
    hotspots = hotspots[:5]

    orphan_residues = [r["id"] for r in residues if not (r.get("applies_to_stressors") or [])]

    state["contagion"] = {
        "couplings": couplings,
        "incidence": incidence,
        "stressor_coverage": stressor_coverage,
        "residue_load": residue_load,
        "coupling_matrix": [[round(v, 3) for v in row] for row in coupling_matrix],
        "brittleness_rank": brittleness_rank,
        "hotspots": hotspots,
        "orphan_residues": orphan_residues,
    }

    text = json.dumps(state, indent=2) + "\n"
    if args.out == "-":
        sys.stdout.write(text)
    else:
        Path(args.out).write_text(text, encoding="utf-8")
    print(f"contagion: residues={len(residues)} stressors={len(stressors)} hotspots={len(hotspots)} orphans={len(orphan_residues)}",
          file=sys.stderr)
    if orphan_residues:
        print(f"WARNING: orphan residues found: {orphan_residues}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
