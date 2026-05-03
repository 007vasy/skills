# Workflow — `iterate` mode

Triggered when the user says "iterate on", "update the analysis", "we have new constraints", "redo with X", "load my previous analysis", or supplies a path to an existing `state.json`.

## Preconditions

- A prior `state.json` exists at `./.residuality/<slug>/state.json` (or wherever the user points).
- The user has stated what changed (a new constraint, a new component, a new market, a new regulatory rule, a new piece of the stack).

## Steps

### 1. Load prior state

```bash
python3 scripts/state_io.py load --path <state_path>
```

The script validates against the schema and prints the JSON. Read it carefully. Note especially:
- `naive_architecture` (what's already mapped)
- `user_stack_facts[]` (what's been confirmed)
- `attractors_residues[]` (prior derivation work — DO NOT silently overwrite)
- `history[]` (prior runs)

### 2. Classify the change

Apply **Block J** from `prompt_templates.md`. Decide which sections the user's new input affects:

| Change | Sections that update |
|---|---|
| New tech in the stack | `user_stack_facts[]` only; downstream unchanged unless a residue's `stack_fit_citations` is now wrong |
| New regulatory / market constraint | `stressors[]` (additive — add new stressors, do not delete prior); new `attractors_residues[]` per added stressor; re-run dedupe; re-run contagion + criticality |
| New component | `naive_architecture`; possibly new stressors; re-run contagion + criticality |
| Removed component | Mark related residues; remove orphans via `contagion_matrix.py`'s orphan check; re-run contagion + criticality |
| New focus / lens | Re-run stressor brainstorm in additive mode under the focus bias |

### 3. Apply additive changes only

**Critical rule:** never delete or overwrite prior `attractors_residues` entries that are still relevant. If a residue is now obsolete, keep its record but annotate `merge_log` with `{kept_id: null, dropped_id: <id>, similarity: -1, reason: "<why obsolete>"}`.

Generate new entries via **Block C + D** (attractor first, residue second) for any newly-added stressors. Append to `attractors_residues[]`.

### 4. Re-run downstream stages

In order:
1. `scripts/residue_dedupe.py` — to merge any new residues into the existing stack.
2. `scripts/contagion_matrix.py` — to re-score with new residues / new couplings.
3. `scripts/criticality_estimate.py` — only if data sufficiency holds.
4. `scripts/report_render.py` — to produce a fresh report with a run-log diff section.

### 5. Append history

When `scripts/state_io.py save` runs, it will append a `history[]` entry. Set `mode: "iterate"`, `note: "<one-line summary of what changed>"`, `changed_sections: [...]` covering exactly the sections you changed.

## Output diffs

The new `report.md` includes a "Run log diff" section near the top showing:
- New stressors added since the previous run.
- New residues added.
- Residues marked obsolete.
- Hotspot / brittleness changes.
- Criticality regime change, if any.

This is what makes iterate mode auditable. Without the diff, the user has no idea what your new run actually changed.

## When iterate doesn't apply

If the change is large enough that re-deriving everything makes more sense than diffing (e.g. a complete pivot of the business), tell the user: *"This change is large enough that I recommend running `analyze` fresh on a new project slug; I'll preserve the prior state for comparison."* — then start a new `analyze` run with a different slug.
