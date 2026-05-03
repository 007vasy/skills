# Criticality guidance — NKP and the edge of chaos

This file defines how `scripts/criticality_estimate.py` computes N, K, P and labels the regime, plus what to recommend when the regime is wrong.

## Background

Stuart Kauffman's NKP model studies how networks of interdependent agents behave under perturbation. Three numbers govern behaviour:

- **N** — number of nodes (here: components in the architecture).
- **K** — average number of dependencies per node (in-degree + out-degree, divided by 2).
- **P** — constraint density on the network's behaviour, normalised 0-1.

Behaviour falls into three regimes:

| Regime | Symptoms | Why it happens |
|---|---|---|
| **Frozen** | Rigid; small changes don't propagate; the system can't adapt to novelty | Too few residues, too tightly coupled to a happy path; or a brittle monolith |
| **Edge of chaos** | Adaptive; perturbations contained but learn-able from | Diverse residues, sensible bulkheads, contagion bounded |
| **Chaotic** | Small perturbations cascade widely; incidents have huge blast radius | Too many couplings, no isolation; one residue's failure triggers many |

The target is the **edge of chaos**. Most production systems start *frozen* (overfit to the happy path) and need stressor-driven residues to climb to the edge.

## How the estimator computes N, K, P

### N — components

Count the entries in `naive_architecture.components[]`. That is N.

### K — average coupling per component

Build the undirected coupling graph from:
1. `naive_architecture.edges[]` — every edge contributes to both endpoints.
2. `state.contagion.coupling_matrix` — for any cell ≥ 0.5, contribute to both endpoints' degree count, weighted by the coupling value.

Compute:
```
K = (sum of weighted degrees) / N
```

For a plain undirected graph this equals `2 * |E| / N`. K is a real number, not an integer. Typical values: 1.5-5.

### P — constraint density

P captures how strongly the system's behaviour is pinned. Sources:
1. Each entry in `naive_architecture.assumptions[]` contributes 0.05 (cap at 0.40).
2. Each `regulatory` or `safety` residue contributes 0.04 (cap at 0.30).
3. Each entry in `state.focus[]` contributes 0.05 (cap at 0.20).
4. Add 0.10 baseline.

Sum, clamp to [0, 1]. P is the constraint density.

## Regime classification

Given (N, K, P), classify:

```
if N < 4:
    regime = "indeterminate — too few components"
elif K < 1.5:
    regime = "frozen"
elif K > 4.5 or P < 0.20:
    regime = "chaotic"
elif 1.5 <= K <= 4.5 and P >= 0.20:
    regime = "edge"
else:
    regime = "edge"  # default safe label
```

Additional gate: require `len(stressors) >= 25` AND `len(residue_stack) >= 8`. If either fails, force `regime = "indeterminate — need more data"` regardless of the K/P math.

## Recommended deltas

When `regime != "edge"`, the script emits suggestions in `criticality.deltas[]`. The skill surfaces them to the user; it does not auto-apply.

### Frozen → edge

Goal: increase K *selectively* by adding decoupling residues and fallback paths, without raising K everywhere.

Suggested deltas:
- Add `circuit_breaker_fallback_cache` at the most-loaded read path (raises K slightly, raises adaptability).
- Add `read_only_degraded_mode` to the write-critical surface that has no fallback today.
- Add a `bulkhead` if one tenant or one downstream can starve the cluster.

Expected NKP shift: K +0.3 to +0.8, P unchanged.

### Chaotic → edge

Goal: reduce K by removing brittle couplings; or raise P by adding constraints.

Suggested deltas:
- Inspect the top entry in `brittleness_rank`; that residue→residue coupling is the first to break. Either decouple them (e.g. introduce a queue) or add a circuit breaker between them.
- Add `tenant_isolated_blast_radius` if a tenant defect can contaminate other tenants.
- Add `audit_log_immutability` if the chaos is in part driven by a lack of investigability.

Expected NKP shift: K −0.5 to −1.0, or P +0.05 to +0.10.

### Edge

Report the regime; no deltas unless the user wants stretch goals (e.g. "what would push us over the edge into chaotic?" — useful as a thought experiment).

## What the estimator deliberately does NOT do

- It does not predict incident frequency.
- It does not assign a "score" to the architecture (no grade A/B/C). The number is N, K, P; the regime is a label; that is all.
- It does not run simulations. NKP here is a heuristic, not a Monte Carlo.

## When to override

If the user knows their domain better than the heuristic (e.g. "we are deliberately frozen because we are a regulated medical device — that is correct"), trust the user. Surface the regime label but accept their override and record the rationale in `open_questions[]`.
