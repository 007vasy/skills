# Prompt templates

Reusable self-prompt blocks. When you reach a step in the core loop, paste the relevant block into your own reasoning and follow its constraints. Each block has explicit guardrails — do not relax them silently. If a guardrail conflicts with reality, surface the conflict to the user; do not paper over it.

---

## Block A — Naive architecture capture

Use this when the user has handed you a fresh system to analyse.

```
Capture the *naive* architecture. Naive means: pre-stress, no resilience theatre, honest about its assumptions.

For each component, record:
- id (C01..C99), name, kind (service|datastore|queue|client|external|human|device|edge)
- 1-line responsibility
- tech_assumptions (only if the user has stated them — never invent)

For each edge:
- from, to, kind (sync|async|data|human|device), 1-line note

Also record:
- summary (3-5 sentences in business language)
- business_context (what is this system FOR, in customer terms)
- assumptions (3-7 things the architecture quietly assumes — e.g. "users have smartphones", "cellular coverage at every site", "the regulator does not change the billing model")

Hard rule: if the user has not specified the tech for a component, write `tech_assumptions: []` and add an entry to `open_questions[]` rather than guessing. Fictional stack is the #1 failure mode.

Output: a single JSON object matching `naive_architecture` in `assets/state_schema.json`.
```

---

## Block B — Stressor brainstorm

Use this in step 2 of the core loop. Generate ≥30 stressors.

```
Generate stressors that perturb the naive architecture. The point is *diversity* and *unexpectedness*, not exhaustiveness.

Process:
1. Open `references/stressor_catalogue.md` for inspiration; never copy verbatim — re-cast each archetype in this user's specific business and tech context.
2. Generate freely first, in the user's domain. Aim for 40 candidates.
3. For each stressor, classify into ONE of the 9 categories from `assets/stressor_categories.json`.
4. Score `novelty` 1-5: 1 = "every architect would list this", 5 = "would not appear in any standard risk register".
5. Set `horizon`: now | 1y | 5y.

Hard requirements (the diversity checker will reject the list otherwise):
- Hit every category floor (regulatory ≥2, market ≥1, tech ≥2, human ≥2, adversarial ≥2, environmental ≥1, supply-chain ≥1, scale ≥2, time ≥1).
- ≥30 stressors total.
- ≥3 stressors with novelty=5 (black-swan / absurd).
- Average novelty ≥ 3.0.
- No stressor described in pure-tech terms — every stressor must include a 1-line business consequence.

Anti-patterns to reject in your own list before saving:
- "AWS region down" with no business consequence.
- "DB outage" — too generic; specify which workload it breaks.
- "Service crashes" — what causes the crash?
- All stressors clustered in tech + scale (likely floor failure).

Output: a JSON array matching `stressors[]` in `assets/state_schema.json`. Then run `scripts/stressor_diversity_check.py` and address any warnings before proceeding.
```

---

## Block C — Attractor extraction

Use this in step 3 of the core loop, once per stressor. Always extract the attractor *before* proposing a residue.

```
For stressor `<S_id>: <name>`, extract the business attractor — where the business state ends up if you do nothing about this stressor.

Rules:
- Attractor name is readable to a non-engineer ("we lose every payment from the last 90 seconds and customers see double-charges"). If yours can't be read by a non-engineer, reword it.
- Attractor description is 1-3 sentences. NOT a fix. NOT a residue. Just: what happens.
- `why_system_drifts_here` names the structural reason — which assumption fails, which path has no fallback, which feedback loop accelerates the slide.

Hard rule: if you cannot describe the attractor in business language, you do not yet understand the stressor. Ask the user a clarifying question instead of guessing.

Output: an `attractor` object matching the schema. Save it; only THEN move to Block D for the residue.
```

---

## Block D — Minimal residue derivation

Use this in step 3 of the core loop, immediately after Block C succeeds.

```
For attractor `<A_name>` from stressor `<S_id>`, propose the MINIMAL residue that lets the business survive the attractor.

Minimal means:
- Smallest viable change to the existing system.
- 1-3 sentences max.
- Has an obvious 1-sentence implementation hint.

Process (in order — do not skip):
1. Open `references/residue_library.md`. Find the closest pattern (`source_pattern` field). If a pattern fits, use it; do not reinvent.
2. If no pattern fits cleanly, you may propose a novel residue — but justify why no library pattern fit.
3. Cite at least one entry from `user_stack_facts[]` this residue is compatible with (`stack_fit_citations`). If you cannot cite any, STOP and ask the user — do not invent a tech the user has not confirmed.
4. List which stressors this residue addresses (`applies_to_stressors`). If only the current one, that is fine; if it covers others, list them too — that is what the dedupe step exploits.
5. Estimate cost: low | med | high.

Hard rules (reject your own draft if any are violated):
- If your residue requires REPLACING a component (DB → different DB, framework → different framework), you have written down another attractor description. Stop. Try again.
- If `stack_fit_citations` is empty, you are inventing a stack. Stop. Ask the user.
- If `applies_to_stressors` is empty, this is theatre. Stop. Either remove it or find the stressor it actually addresses.
- If `estimated_cost == "high"`, you almost certainly violated the minimality rule. Re-check.

Output: a `residue` object matching the schema, paired with the attractor as an `attractor_residue` entry.
```

---

## Block E — Stack and dedupe

Use this in step 4 of the core loop, after every stressor has an attractor + residue.

```
The same residue often surfaces under multiple stressors — that is the point. Collapse them.

Process:
1. Collect all residues from `attractors_residues[].residue` into a list.
2. Run `scripts/residue_dedupe.py --in <state.json> --out <state.json>` (it operates in-place on the residue_stack section).
3. Read the `merge_log` it emits. For any merge with similarity 0.75-0.85 (the marginal band), eyeball the pair and confirm the merge is correct; if not, undo via the dedupe tool's `--keep-both <id1> <id2>` flag.
4. The resulting `residue_stack[]` should have ~40-70% the count of the raw list. If it is closer to 100%, you under-merged; if closer to 20%, you probably over-merged.
5. Each entry in `residue_stack[]` MUST keep its full union of `applies_to_stressors` from the merged sources, and `merge_log[]` records what was dropped into it.
```

---

## Block F — Contagion scoring

Use this in step 5 of the core loop, after dedupe.

```
Build the contagion picture.

Process:
1. For each pair of residues (R_i, R_j), decide if they share components or assumptions:
   - Same component touched? coupling_weight 0.4-0.6.
   - Shared tacit assumption (e.g. both rely on cellular connectivity, both rely on the user having a smartphone)? coupling_weight 0.3-0.5.
   - One residue's failure mode IS the other's stressor? coupling_weight 0.7-0.9.
   - Otherwise omit the entry.
2. For every coupling include a `reason` ≤ 1 sentence. No reason → no coupling.
3. Run `scripts/contagion_matrix.py --in <state.json> --out <state.json>`.
4. Read the output:
   - `hotspots[]`: top-quartile residues by load × brittleness. These are doing too much; they are tomorrow's incident.
   - `brittleness_rank[]`: the residue→residue couplings most likely to cascade.
   - `orphan_residues[]`: MUST be empty in a valid state. If non-empty you have a theatre-residue; remove it or find its real stressor.

Hard rule: surface the 3-bullet narrative ("Most-loaded residue: X, addresses N stressors. Most brittle coupling: Y → Z. Lowest-coverage stressor: S.") in the report BEFORE any matrix table. Numbers without narrative are wallpaper.
```

---

## Block G — Criticality estimation

Use this in step 6 of the core loop, after contagion.

```
Estimate where the residue-augmented architecture sits on the criticality spectrum.

Process:
1. Confirm the data is sufficient: ≥25 stressors AND ≥8 distinct residues in the stack. If not, set `regime: "indeterminate — need more data"` and stop.
2. Run `scripts/criticality_estimate.py --in <state.json> --out <state.json>`.
3. Read the output:
   - `N`: number of components.
   - `K`: average coupling per component.
   - `P`: constraint density (0-1).
   - `regime`: frozen | edge | chaotic.
   - `deltas[]`: suggested moves with expected NKP shift.
4. If `regime == "frozen"`: the architecture is rigid and brittle to novelty. Proposed deltas typically add residues that decouple a hotspot or introduce a fallback path.
5. If `regime == "chaotic"`: the architecture cascades easily. Proposed deltas typically add bulkheads or remove a brittle coupling.
6. If `regime == "edge"`: report it; no automatic deltas needed unless the user wants a stretch goal.

See `references/criticality_guidance.md` for the heuristics behind N, K, P thresholds.
```

---

## Block H — Report rendering

Use this in step 7 of the core loop, last.

```
Render the report.

Process:
1. Run `scripts/report_render.py --in <state.json> --out-dir ./.residuality/<project>/`.
2. It produces:
   - `report.md` (the human-facing artefact)
   - `architecture_before.mmd` and `architecture_after.mmd` (Mermaid)
   - `contagion.csv` (full matrix for power users)
   - `summary.json` (machine-readable digest)
3. Open `report.md`. Confirm:
   - The exec summary is 3 bullets max.
   - Every section has content or an explicit `_No data — see workflow step N_` placeholder. Empty sections must NOT be silently fabricated.
   - No `orphan_residues` appear in the residue stack section.
   - No residue without `stack_fit_citations` made it through.
4. If iterating, the report includes a run-log diff section showing what changed since the previous run.
```

---

## Block I — Wizard turn

Use this when the user asked for wizard mode. ≤3 questions per turn; never ask everything at once.

```
You are in wizard mode. Walk the user through capturing the naive architecture interactively.

Pacing:
- Maximum 3 questions per turn. If you have 5 things to ask, ask the most-blocking 3 now and the rest after the user responds.
- Questions are open-ended and grounded ("what does the customer see when they pay?", not "what is your payment architecture?").
- After each turn, re-render the partial `naive_architecture` and `user_stack_facts` so the user can see what you have learned.

Question buckets, in priority order:
1. Business context: who uses this, what for, what is the moment of value?
2. The happy path: walk me through one successful end-to-end interaction.
3. Components and edges: what does each step actually call?
4. The stack: which datastores, which message brokers, which clouds, which third parties?
5. Constraints: regulators, latency budgets, cost ceilings, geography.
6. Pains: what currently scares you about this system at 3 a.m.?

Move to stressor brainstorm only when:
- Every component has a name and kind.
- Every edge has from, to, kind.
- `user_stack_facts[]` has ≥3 confirmed entries.
- `business_context` is filled.
```

---

## Block J — Iterate-mode diff

Use this when the user has supplied (or you have located) a prior `state.json` and given new constraints.

```
You are iterating on a prior run. Do not re-run the full loop blindly.

Process:
1. Run `scripts/state_io.py load --path <state_path>` to read the prior state.
2. Read the user's new constraints carefully. Decide which sections they affect:
   - New tech in the stack? → update `user_stack_facts[]` only; nothing downstream changes unless it invalidates a residue.
   - New regulatory constraint or new market? → re-run stressor brainstorm in *additive* mode (add new stressors, do not delete prior); new attractor+residue per added stressor; re-run dedupe; re-run contagion + criticality.
   - New component in the architecture? → update `naive_architecture`, then re-run contagion + criticality. Stressors may need additions.
   - Removed component? → mark related residues as `applies_to_stressors: []`-checked; remove orphans; re-run contagion + criticality.
3. Append a `history[]` entry with this turn's `mode: "iterate"`, `note: "<one line>"`, `changed_sections: [...]`.
4. Save with `scripts/state_io.py save`. Re-render the report.

Hard rule: never overwrite or delete prior `attractors_residues` entries that are still relevant. If a residue is now obsolete, keep it but mark `merge_log` with `dropped_id: <id>, kept_id: null, similarity: -1` and a `reason`.
```

---

## Block K — Contagion-only

Use this when the user has supplied an existing residue list and wants only the matrix.

```
You are in contagion-only mode. Skip steps 2 and 3 of the core loop.

Inputs you need from the user:
- `naive_architecture` (or a sketch — components + edges suffice)
- `user_stack_facts[]`
- A list of residues with at least: id, name, intent, applies_to_stressors[], stack_fit_citations[]
- Optional: a list of stressors (if the residues reference them); otherwise infer minimal stressor placeholders from `applies_to_stressors`.
- Optional: a couplings[] list. If absent, infer couplings via Block F process and surface them for user confirmation before computing the matrix.

Then:
1. Run `scripts/residue_dedupe.py` (the user's list may have duplicates).
2. Run `scripts/contagion_matrix.py`.
3. Run `scripts/criticality_estimate.py` only if there are ≥8 deduped residues.
4. Run `scripts/report_render.py` with sections for stressor-generation marked `_Skipped — contagion-only mode_`.
```

---

## Block L — Focus biasing

Use this on top of any of the blocks above when the user has specified `--focus <area>` or an equivalent natural-language hint.

```
You are biasing the analysis toward <focus_area> ∈ {security, cost, regulatory, performance, safety}.

Apply the weight table from `references/focus_biasing.md`:
- Stressor brainstorm (Block B): bias generation toward the focus area's high-weight categories. The category floors from `assets/stressor_categories.json` STILL APPLY — bias adds, never removes.
- Residue derivation (Block D): prefer library patterns from the focus area's preferred list when more than one fits.
- Report render (Block H): the exec summary leads with the focus-area framing.

Hard rule: focus is a bias, not a filter. A stressor outside the focus area that is critical to the business stays in.
```
