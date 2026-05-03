---
name: residuality
description: This skill should be used when the user asks to "do a residuality analysis", "apply Residuality Theory", "stress-test this architecture", "find architectural residues", "build a contagion matrix", "what stressors should I worry about", "make this architecture resilient", "Barry O'Reilly residues", or mentions naive vs residual architecture, attractors, edge of chaos, or NKP for software design. Activates for whole-architecture stress reviews; not for line-level code review or single-component refactors.
version: 0.1.0
---

# Residuality Theory for Software Architecture

This skill operationalises Barry O'Reilly's Residuality Theory (GOTO Copenhagen 2025): take a *naive* architecture, stress-test it against deliberately diverse stressors, derive **attractors** (where the business state ends up if you do nothing) and the smallest **residues** (architectural changes) that survive each attractor, stack and dedupe the residues, then run **contagion** analysis to surface dangerous hidden couplings. The deliverable is a Markdown + Mermaid + JSON report and a persistent `state.json` you can iterate on.

## When to use this skill

**Use it for:**
- Whole-architecture resilience reviews of a new or existing system.
- Auditing a vendor or team architecture proposal before commitment.
- Pre-mortem before a major release or an entry into a new market / region / regulatory regime.

**Do not use it for:**
- Line-level code review or single-component refactors (use `/review` or a code-review subagent).
- Performance tuning of one hot path (use a profiler-driven workflow).
- Generic "is this architecture good?" without a specific system to analyse.

## Read this first — at the top of every run

Always load **`references/watchouts.md`** before doing anything else. It lists the eight failure modes this skill exists to prevent (boring stressors, residue-as-rewrite, fictional stack, theatre-residues, wall-of-numbers contagion, history overwrite, jargon drift, premature criticality verdict). The rest of the skill is built around guarding against these.

Also load **`references/theory_primer.md`** once per project to establish vocabulary (stressor / attractor / residue / contagion / NKP / edge of chaos).

## Mode detection

Detect mode from the user's phrasing. Modes compose (`wizard` + focus, etc.).

| Mode | Trigger phrases | Workflow file to load |
|---|---|---|
| `analyze` (default) | "residuality analysis", "stress-test this architecture", "find residues", "make this resilient" | `references/workflow_analyze.md` |
| `wizard` | "walk me through", "interview me", "wizard mode", "I don't know my architecture yet" | `references/workflow_wizard.md` |
| `iterate` | "iterate on", "update the analysis", "new constraints", "redo with X", or a path to an existing `state.json` is supplied | `references/workflow_iterate.md` |
| `contagion-only` | "contagion only", "just compute the matrix", "score these residues", "skip stressor generation" | `references/workflow_contagion_only.md` |
| focus biasing (overlay) | "focus on security", "we care most about cost", "regulatory lens", explicit `--focus <area>` | `references/focus_biasing.md` (apply on top of the chosen workflow) |

## Core loop (always run in this order in `analyze` mode)

1. **Capture naive architecture.** Apply Block A from `references/prompt_templates.md`. Components + edges + business context + assumptions. Populate `user_stack_facts[]` from confirmed tech only — never invent.
2. **Generate stressors.** Apply Block B. ≥30 stressors hitting all 9 category floors from `assets/stressor_categories.json`, ≥3 black swans, average novelty ≥ 3.0. Verify via `scripts/stressor_diversity_check.py`.
3. **Per stressor, derive attractor + residue.** Apply Block C (attractor first, business language) then Block D (minimal residue with `stack_fit_citations` from `user_stack_facts`).
4. **Stack and dedupe.** Apply Block E. Run `scripts/residue_dedupe.py`. Eyeball marginal merges (similarity 0.55-0.85).
5. **Contagion analysis.** Apply Block F. Add explicit `couplings[]` for known shared components / shared assumptions / failure-of-X-is-stressor-for-Y links. Run `scripts/contagion_matrix.py`. **Surface and resolve any `orphan_residues`** — they signal theatre-residues.
6. **Criticality estimate.** Apply Block G. Run `scripts/criticality_estimate.py`. Surface deltas if regime is `frozen` or `chaotic`; user decides whether to act.
7. **Render report.** Apply Block H. Run `scripts/report_render.py --in <state.json> --out-dir ./.residuality/<project>/`. Verify against `references/watchouts.md`.

Save state with `scripts/state_io.py save` between major stages — it appends to `history[]` so iterate mode has an audit trail.

## When to load which reference

| Step in the loop | Reference to load |
|---|---|
| Top of run | `references/watchouts.md` |
| First time on a project | `references/theory_primer.md` |
| Step 1 (naive architecture) | Block A from `prompt_templates.md` |
| Step 2 (stressor generation) | `references/stressor_catalogue.md` + Block B |
| Step 3 (attractor + residue) | `references/residue_library.md` + Blocks C and D |
| Step 4 (dedupe) | Block E |
| Step 5 (contagion) | Block F + report-format expectations from `references/report_format.md` |
| Step 6 (criticality) | `references/criticality_guidance.md` + Block G |
| Step 7 (render) | `references/mermaid_diagram_guide.md`, `references/report_format.md`, Block H |
| Wizard mode | `references/workflow_wizard.md` + Block I |
| Iterate mode | `references/workflow_iterate.md` + Block J |
| Contagion-only mode | `references/workflow_contagion_only.md` + Block K |
| Any focus bias | `references/focus_biasing.md` + Block L |
| Verification / first-time learning | `references/ev_charging_walkthrough.md` |

## Outputs

Default location `./.residuality/<project-slug>/`:
- `state.json` — full run state (machine-readable; the source of truth for iterate mode).
- `report.md` — human-facing Markdown report.
- `architecture_before.mmd` — Mermaid of the naive architecture.
- `architecture_after.mmd` — Mermaid with residue overlays and hotspot styling.
- `contagion.csv` — full residue × residue coupling matrix.
- `summary.json` — digest (criticality, hotspots, low-coverage stressors).

## State and iteration

The `state.json` schema is at `assets/state_schema.json`. Every save appends a `history[]` entry so prior runs are auditable. **Iterate mode never silently overwrites prior `attractors_residues`** — obsolete residues are marked in `merge_log` rather than deleted.

`user_stack_facts[]` is mandatory before residue derivation. Residues without `stack_fit_citations` are rejected by the schema. This kills the fictional-stack failure mode.

## Verification

`references/ev_charging_walkthrough.md` is the **gold reference**. The skill should be able to reproduce its key findings end-to-end on the EV charging fixture at `tests/fixtures/ev_charging.json`:

- All 9 stressor categories met; diversity check passes (with the expected note about black-swan count).
- ALPR fallback, per-minute billing, local autonomy / circuit breakers, charge-session observability, unlock redundancy, async-reconciliation outbox **all** appear in the residue stack.
- ALPR fallback (R02), local autonomy (R01), and observability (R05) appear in `hotspots[]`.
- Top brittleness coupling: R06 (outbox) ↔ R14 (idempotent webhook), Stripe-event-semantics shared.
- Criticality: regime `edge`, N in 8-14, K in 1.5-3.

If a real run misses any of these, investigate before declaring success.

## Bundled resources

- `references/` — theory, workflow per mode, stressor catalogue, residue library, prompt templates, focus biasing, criticality guidance, Mermaid + report formatting, EV gold walkthrough, watchouts.
- `scripts/` (Python 3.11+, stdlib only, JSON in/out) — `state_io.py`, `stressor_diversity_check.py`, `residue_dedupe.py`, `contagion_matrix.py`, `criticality_estimate.py`, `report_render.py`.
- `assets/` — `state_schema.json` (JSON Schema 2020-12), `stressor_categories.json` (9 categories with min counts), `report_template.md`, `mermaid_before.tmpl`, `mermaid_after.tmpl`.
- `tests/fixtures/ev_charging.json` — gold EV-charging fixture for verification dry-runs.

Run scripts as `python3 scripts/<name>.py --help` from the skill root for usage. All scripts read/write the state JSON described in `assets/state_schema.json`; chain them via `--in <path> --out <path>` or pipe via stdin/stdout.
