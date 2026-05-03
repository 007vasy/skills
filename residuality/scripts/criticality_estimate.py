#!/usr/bin/env python3
"""Criticality (NKP) estimator.

Implements the heuristic from references/criticality_guidance.md:
  - N: number of components in naive_architecture.components
  - K: average undirected weighted degree from naive edges + significant
       contagion couplings (>= 0.5)
  - P: constraint density (assumptions, regulatory/safety residues, focus areas)

Then classifies regime (frozen | edge | chaotic | indeterminate ...) and emits
recommended deltas for off-edge regimes.

Data-sufficiency gate: requires len(stressors) >= MIN_STRESSORS AND
len(residue_stack) >= MIN_RESIDUES, else regime = "indeterminate — need more data".

Stdlib only.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

MIN_STRESSORS = 25
MIN_RESIDUES = 8
COUPLING_SIGNIFICANT = 0.5

# Regime thresholds (see references/criticality_guidance.md)
K_FROZEN_MAX = 1.5
K_CHAOTIC_MIN = 4.5
P_CHAOTIC_MAX = 0.20

# P contributions
P_BASELINE = 0.10
P_PER_ASSUMPTION = 0.05
P_ASSUMPTION_CAP = 0.40
P_PER_REG_SAFETY_RESIDUE = 0.04
P_REG_SAFETY_CAP = 0.30
P_PER_FOCUS = 0.05
P_FOCUS_CAP = 0.20

REGULATORY_PATTERNS = {
    "audit_log_immutability",
    "event_sourcing_audit_trail",
    "per_minute_billing_path",
    "manual_override_with_review",
}
SAFETY_PATTERNS = {
    "unlock_redundancy",
    "local_autonomy",
    "alpr_camera_fallback_identity",
    "runbook_as_code",
}


def compute_N(state: dict) -> int:
    return len((state.get("naive_architecture") or {}).get("components") or [])


def compute_K(state: dict) -> float:
    arch = state.get("naive_architecture") or {}
    components = arch.get("components") or []
    if not components:
        return 0.0
    comp_ids = {c["id"] for c in components}
    degree: dict[str, float] = defaultdict(float)
    for e in arch.get("edges") or []:
        if e.get("from") in comp_ids and e.get("to") in comp_ids:
            degree[e["from"]] += 1.0
            degree[e["to"]] += 1.0
    # contagion couplings: each significant coupling contributes to the components
    # touched by both residues
    contagion = state.get("contagion") or {}
    matrix = contagion.get("coupling_matrix") or []
    residues = state.get("residue_stack") or []
    # Build residue -> components-touched mapping. We don't have an explicit
    # mapping, so we approximate: any component referenced in the residue's
    # minimal_change_description by id. If unavailable, skip contagion contribution.
    name_to_id = {c["name"].lower(): c["id"] for c in components if c.get("name")}
    tech_to_id: dict[str, str] = {}
    for c in components:
        for ta in c.get("tech_assumptions") or []:
            for tok in ta.lower().split():
                if len(tok) >= 4 and tok.isalpha():
                    tech_to_id.setdefault(tok, c["id"])
    res_components: list[set[str]] = []
    for r in residues:
        text = " ".join([
            r.get("minimal_change_description", ""),
            r.get("intent", ""),
            r.get("name", ""),
        ])
        text_lower = text.lower()
        ids_found = {cid for cid in comp_ids if cid in text}
        for nm, cid in name_to_id.items():
            if nm in text_lower:
                ids_found.add(cid)
        for tok, cid in tech_to_id.items():
            if tok in text_lower:
                ids_found.add(cid)
        res_components.append(ids_found)
    for i, row in enumerate(matrix):
        for j, w in enumerate(row):
            if i >= j or w < COUPLING_SIGNIFICANT:
                continue
            shared = res_components[i] | res_components[j] if i < len(res_components) and j < len(res_components) else set()
            for cid in shared:
                degree[cid] += w
    total = sum(degree.values())
    # Average undirected degree: sum_of_degrees / N (sum_of_degrees = 2|E| for plain graphs).
    return round(total / len(components), 3)


def compute_P(state: dict) -> float:
    arch = state.get("naive_architecture") or {}
    p = P_BASELINE
    p_assumptions = min(P_ASSUMPTION_CAP, P_PER_ASSUMPTION * len(arch.get("assumptions") or []))
    p_reg_safety_count = sum(
        1 for r in (state.get("residue_stack") or [])
        if r.get("source_pattern") in REGULATORY_PATTERNS | SAFETY_PATTERNS
    )
    p_reg_safety = min(P_REG_SAFETY_CAP, P_PER_REG_SAFETY_RESIDUE * p_reg_safety_count)
    p_focus = min(P_FOCUS_CAP, P_PER_FOCUS * len(state.get("focus") or []))
    return round(min(1.0, p + p_assumptions + p_reg_safety + p_focus), 3)


def classify(N: int, K: float, P: float) -> str:
    if N < 4:
        return "indeterminate — too few components"
    if K < K_FROZEN_MAX:
        return "frozen"
    if K > K_CHAOTIC_MIN or P < P_CHAOTIC_MAX:
        return "chaotic"
    if K_FROZEN_MAX <= K <= K_CHAOTIC_MIN and P >= P_CHAOTIC_MAX:
        return "edge"
    return "edge"


def deltas_for(regime: str, state: dict, K: float, P: float) -> list[dict]:
    out: list[dict] = []
    if regime.startswith("indeterminate"):
        return out
    contagion = state.get("contagion") or {}
    if regime == "frozen":
        out.append({
            "action": "Add a circuit_breaker_fallback_cache at the most-loaded read path",
            "expected_NKP_shift": "K +0.3 to +0.6, P unchanged",
        })
        out.append({
            "action": "Add a read_only_degraded_mode for the write-critical surface that has no fallback today",
            "expected_NKP_shift": "K +0.2 to +0.5, P unchanged",
        })
        out.append({
            "action": "Add a bulkhead if any tenant or downstream can starve the cluster",
            "expected_NKP_shift": "K +0.2 to +0.4, P +0.04",
        })
    elif regime == "chaotic":
        # surface the top brittleness pair if available
        ranked = contagion.get("brittleness_rank") or []
        if ranked:
            top = ranked[0]
            out.append({
                "action": f"Decouple {top['residue_id']} from its most-coupled neighbour (see brittleness_rank)",
                "expected_NKP_shift": "K -0.5 to -1.0",
            })
        out.append({
            "action": "Add tenant_isolated_blast_radius if a tenant defect can contaminate other tenants",
            "expected_NKP_shift": "K -0.3, P +0.04",
        })
        out.append({
            "action": "Add audit_log_immutability if chaos is partly driven by a lack of investigability",
            "expected_NKP_shift": "K unchanged, P +0.05",
        })
    return out


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Estimate NKP / criticality regime")
    p.add_argument("--in", dest="in_", default="-", help="path to state.json or '-'")
    p.add_argument("--out", default="-", help="path to write updated state.json or '-'")
    args = p.parse_args(argv)

    if args.in_ and args.in_ != "-":
        state = json.loads(Path(args.in_).read_text(encoding="utf-8"))
    else:
        state = json.loads(sys.stdin.read())

    n_stressors = len(state.get("stressors") or [])
    n_residues = len(state.get("residue_stack") or [])

    if n_stressors < MIN_STRESSORS or n_residues < MIN_RESIDUES:
        regime = f"indeterminate — need more data (have {n_stressors} stressors, {n_residues} residues; need {MIN_STRESSORS} and {MIN_RESIDUES})"
        N = compute_N(state)
        K = compute_K(state)
        P = compute_P(state)
        deltas = []
    else:
        N = compute_N(state)
        K = compute_K(state)
        P = compute_P(state)
        regime = classify(N, K, P)
        deltas = deltas_for(regime, state, K, P)

    state["criticality"] = {
        "N": N,
        "K": K,
        "P": P,
        "regime": regime,
        "deltas": deltas,
    }

    text = json.dumps(state, indent=2) + "\n"
    if args.out == "-":
        sys.stdout.write(text)
    else:
        Path(args.out).write_text(text, encoding="utf-8")
    print(f"criticality: N={N} K={K} P={P} regime={regime!r} deltas={len(deltas)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
