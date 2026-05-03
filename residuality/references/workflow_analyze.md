# Workflow — `analyze` (default mode)

This is the default mode of the skill. Trigger phrases include "do a residuality analysis", "stress-test this architecture", "find architectural residues", "make this architecture resilient".

## Preconditions

Before running, you must have:
- A description of the system (the user's prompt should provide this; if not, switch to `wizard` mode).
- An understanding of who the user is (engineer, architect, product owner) — adapt language.

## Steps (run in order, never skip)

### 1. Load context

Load these references into context, in order:
1. `references/watchouts.md` — re-read the failure modes; you will check yourself against them throughout.
2. `references/theory_primer.md` — establish vocabulary.
3. `references/stressor_catalogue.md` — for the brainstorm step (held in mind, not blindly copied).
4. `references/prompt_templates.md` — keep open; you will use Blocks A–H.

### 2. Initialise state

Run `scripts/state_io.py init --project "<slug>" --path ./.residuality/<slug>/state.json`. This creates an empty state file with `schema_version: "1.0"`, current timestamps, and `mode: "analyze"`.

### 3. Capture naive architecture

Apply **Block A** from `prompt_templates.md`. Output goes into `state.naive_architecture`. Add to `state.user_stack_facts[]` every concrete tech detail the user has confirmed. Save state.

If `user_stack_facts[]` ends with fewer than 3 entries, ask the user 1-2 clarifying questions. Residue derivation will be unreliable without them.

### 4. Generate stressors

Apply **Block B** from `prompt_templates.md`. Aim for 30-45 stressors. Save into `state.stressors[]`.

Run the diversity check:
```bash
python3 scripts/stressor_diversity_check.py --in ./.residuality/<slug>/state.json
```

If the script reports `missing_categories` or `boring_score` above threshold, return to Block B and fill the gaps. Do NOT proceed to step 5 until the diversity check passes.

### 5. Per-stressor attractor + residue

For each stressor in `state.stressors[]`:
1. Apply **Block C** to extract the attractor.
2. Apply **Block D** to derive the minimal residue.
3. Append to `state.attractors_residues[]`.

You may batch this in groups of 5-10 stressors per turn for context efficiency, but never skip the attractor step (Block C) or jump straight to a residue.

After each batch, save state via `scripts/state_io.py save`.

### 6. Stack and dedupe

Apply **Block E**. Run:
```bash
python3 scripts/residue_dedupe.py --in ./.residuality/<slug>/state.json --out ./.residuality/<slug>/state.json
```

Read the `merge_log`. Confirm marginal merges (similarity 0.75-0.85) by eyeball.

### 7. Contagion analysis

Apply **Block F**. For every meaningful residue pair, decide if a coupling exists; record into `state.contagion.couplings[]` (this is added to the state pre-script). Then run:
```bash
python3 scripts/contagion_matrix.py --in ./.residuality/<slug>/state.json --out ./.residuality/<slug>/state.json
```

Read `hotspots`, `brittleness_rank`, `orphan_residues`. **`orphan_residues` MUST be empty** — if not, you have theatre-residues; fix them before continuing.

### 8. Criticality estimate

Apply **Block G**. Run:
```bash
python3 scripts/criticality_estimate.py --in ./.residuality/<slug>/state.json --out ./.residuality/<slug>/state.json
```

If the regime is `frozen` or `chaotic`, surface the suggested deltas to the user. They are not auto-applied; the user decides.

### 9. Render report

Apply **Block H**. Run:
```bash
python3 scripts/report_render.py --in ./.residuality/<slug>/state.json --out-dir ./.residuality/<slug>/
```

Open `report.md`. Verify against the watchout checklist. Report-back to the user with a brief summary plus the path.

### 10. Append history

`scripts/state_io.py save` will already have appended a `history[]` entry tagged `mode: "analyze"`. Confirm `changed_sections` covers what you actually changed.

## Outputs

- `./.residuality/<slug>/state.json` — full state, machine-readable
- `./.residuality/<slug>/report.md` — human report
- `./.residuality/<slug>/architecture_before.mmd` — Mermaid of naive arch
- `./.residuality/<slug>/architecture_after.mmd` — Mermaid with residue overlays
- `./.residuality/<slug>/contagion.csv` — full matrix
- `./.residuality/<slug>/summary.json` — digest

## When to break this workflow

- The user mid-flight says "actually, I want to focus on security" → load `focus_biasing.md` and re-run from step 4 with the bias applied.
- The user mid-flight reveals new tech that contradicts a residue you proposed → switch to **iterate** mode for the next turn; do not silently overwrite.
- The user wants only the contagion matrix on a hand-supplied residue list → switch to **contagion-only**.
