# Watch-outs (read at the top of every run)

These are the failure modes Residuality work tends to fall into. Re-check yourself against this list at every step. Each item names the trap, why it happens, and the explicit guard already baked into the skill.

## 1. Boring stressors

**Trap.** The stressor list collapses to safe, generic infrastructure failures: "AWS region down", "DB outage", "service crashes", "deploy fails". The output is a resilience report any architect could have written without you.

**Why it happens.** Tech-trained brains reach for tech failures first. LLMs reach for the most-discussed examples in their training data, which are the safe ones.

**Guard.**
- `references/stressor_catalogue.md` enforces 9 categories with minimum counts; you must hit every floor.
- The brainstorm prompt in `references/prompt_templates.md` mandates ≥1 adversarial, ≥1 regulatory, ≥1 human-error, ≥1 supply-chain stressor, and rewards `novelty ≥ 4`.
- `scripts/stressor_diversity_check.py` will reject the list and emit `missing_categories` + suggestions if the floor is missed or `boring_score` is high.
- Include at least 3 black-swan / absurd stressors per `prompt_templates.md`.

## 2. Residues drift into rewrites

**Trap.** "The residue for region outage is to re-architect onto multi-region active-active with cross-region replication and conflict resolution." That is not a residue. That is a new attractor description disguised as a fix.

**Why it happens.** Engineers like clean architectures. Given a stressor, the temptation is to redesign around it.

**Guard.**
- The minimal-residue derivation block in `references/prompt_templates.md` hard-constrains: *smallest viable change to the existing system; if your residue requires replacing a component, you have an attractor description, not a residue — stop and try again.*
- `references/residue_library.md` patterns are minimal by construction (Outbox, Bulkhead, Circuit Breaker w/ Fallback Cache, Read-Only Degraded Mode, Idempotent Replay). Reach for one of these before inventing.
- Residues with `estimated_cost: high` are flagged in the report with a warning footnote — treat that as a smell, not a feature.

## 3. Wall-of-numbers contagion matrix

**Trap.** The contagion section becomes a 25×25 grid of numbers nobody reads. The valuable signal — *which residues are doing too much; which couplings are dangerous* — is buried.

**Why it happens.** Matrices look impressive. Narratives feel less rigorous.

**Guard.**
- `scripts/contagion_matrix.py` always emits `hotspots` (top-quartile residues by load×brittleness, max 5) and `brittleness_rank` (top 5 residue→residue couplings).
- `references/report_format.md` requires the matrix section to lead with a 3-bullet narrative ("Most-loaded residue: X, addresses N stressors. Most brittle coupling: Y → Z. Lowest-coverage stressor: S.") *before* any table.

## 4. Fictional stack

**Trap.** The skill recommends "use NATS JetStream for the outbox" when the user is on Postgres-only with no message broker. The recommendation is technically valid but operationally unmoored.

**Why it happens.** LLMs invent technologies that fit the pattern, not the user's reality.

**Guard.**
- The state file requires a non-empty `user_stack_facts[]` before residue derivation.
- The residue prompt block in `references/prompt_templates.md` requires every residue to cite at least one entry from `user_stack_facts` it is compatible with. If none, the rule is *ask the user; do not invent*.
- The state schema enforces `stack_fit_citations` with `minItems: 1` — you cannot save a residue without at least one citation.

## 5. Theatre-residues

**Trap.** A residue is added because it sounds wise — "comprehensive observability platform", "central audit log" — but it doesn't actually address any stressor on the list.

**Why it happens.** Best-practice reflexes. The residue exists to make the report feel complete.

**Guard.**
- The state schema requires `applies_to_stressors` with `minItems: 1`.
- `scripts/contagion_matrix.py` emits `orphan_residues` (any residue with empty coverage) — a non-empty orphan list is a hard failure.
- `scripts/report_render.py` refuses to render orphan residues into the residue stack section.

## 6. Iterate mode silently overwrites history

**Trap.** Re-running with new constraints quietly drops the prior residues, the team has no audit trail of what changed and why.

**Why it happens.** Re-derivation is convenient; preserving prior runs takes discipline.

**Guard.**
- `scripts/state_io.py save` always appends to `history[]` and never replaces prior entries in `attractors_residues`.
- Every save tags `updated_at` and best-effort `git_sha`.
- `scripts/report_render.py` includes a run-log diff section showing what changed between this run and the previous.

## 7. Business language drifts into jargon

**Trap.** Stressors and attractors are written as technical events ("Kafka rebalance event", "TCP RST flood"). The business reader can't engage.

**Why it happens.** Technical specificity feels safer than business framing.

**Guard.**
- `references/theory_primer.md` opens with the business-first language rule.
- The stressor brainstorm block in `references/prompt_templates.md` reframes any tech-only stressor as "what does this do to the business?" before accepting it.
- Attractor names should be readable to a non-engineer ("queue grows faster than service", "we lose customers because the charger won't unlock"). If yours can't be, reword it.

## 8. Premature criticality verdict

**Trap.** Calling the system "edge of chaos" with too few residues, or "frozen" because you only generated 3 stressors. The NKP estimate is meaningless until the residue stack is real.

**Why it happens.** The NKP language is alluring; people want to apply it early.

**Guard.**
- `scripts/criticality_estimate.py` runs after `residue_stack` is populated and deduped, never before.
- `references/criticality_guidance.md` documents the minimum: at least 25 stressors and 8 distinct residues before the regime label is meaningful.
- If thresholds aren't met the report shows `regime: "indeterminate — need more data"` rather than guessing.
