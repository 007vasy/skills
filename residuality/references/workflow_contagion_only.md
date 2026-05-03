# Workflow — `contagion-only` mode

Triggered when the user says "contagion only", "just compute the matrix", "score these residues", "skip stressor generation". The user already has a residue list and wants the matrix and any hidden coupling risks.

## Preconditions

The user must supply (or you must extract from their message):
- A description of the architecture (components + edges suffice — full naive arch ideal).
- `user_stack_facts[]` — at least 3 confirmed tech facts.
- A list of residues (at least: `id`, `name`, `intent`, `applies_to_stressors[]`, `stack_fit_citations[]`).
- Optionally: stressors. If absent, infer minimal placeholders from `applies_to_stressors`.
- Optionally: explicit `couplings[]`. If absent, you will infer them and surface for user confirmation.

If any of the required pieces are missing, ask 1-2 questions to fill them. Do not invent.

## Steps

### 1. Initialise state

```bash
python3 scripts/state_io.py init --project "<slug>" --path ./.residuality/<slug>/state.json
```

Set `mode: "contagion-only"` (the script accepts a `--mode` flag for this).

### 2. Populate from user input

Fill in:
- `naive_architecture` (from user description)
- `user_stack_facts[]`
- `residue_stack[]` (the user's residue list — this is unusual; in other modes residues come from `attractors_residues[].residue`)
- `stressors[]` — if the user supplied any, copy them; otherwise generate placeholders for any stressor IDs referenced in `applies_to_stressors` with `category` and `description` marked as `_inferred from residue coverage_`.

`attractors_residues[]` stays empty in this mode. The report will mark stressor-generation and attractor-extraction sections as `_Skipped — contagion-only mode_`.

### 3. Dedupe the user's residue list

User-supplied residue lists are usually noisy.

```bash
python3 scripts/residue_dedupe.py --in ./.residuality/<slug>/state.json --out ./.residuality/<slug>/state.json
```

Surface the merge log to the user. Confirm marginal merges before proceeding.

### 4. Infer couplings (if not supplied)

Apply **Block F** from `prompt_templates.md`. For each residue pair, decide if they share components or assumptions and propose a coupling. Surface the proposed `couplings[]` to the user with reasons; ask them to confirm or correct before computing the matrix.

### 5. Compute matrix

```bash
python3 scripts/contagion_matrix.py --in ./.residuality/<slug>/state.json --out ./.residuality/<slug>/state.json
```

Read `hotspots`, `brittleness_rank`, `orphan_residues`. **Surface `orphan_residues` to the user explicitly** — these are the residues that don't address any stressor in their list, which is a finding in itself.

### 6. Criticality (only if data is sufficient)

Run `scripts/criticality_estimate.py` only if `len(residue_stack) >= 8`. Otherwise set `regime: "indeterminate — need more data"`.

### 7. Render report

```bash
python3 scripts/report_render.py --in ./.residuality/<slug>/state.json --out-dir ./.residuality/<slug>/
```

The report will have stressor-generation and attractor sections marked as skipped. The contagion section will be the centrepiece — that's what the user asked for.

## What this mode is good for

- Auditing an existing resilience design before a major release.
- Reviewing a vendor's architecture proposal.
- Sanity-checking a list of "best practices" the team has accumulated over years to see whether they actually fit together.

## What this mode is NOT good for

- Discovering new stressors you missed (use `analyze`).
- Building a residue stack from scratch (use `analyze` or `wizard`).
