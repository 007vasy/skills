# Residuality report — {{project}}

- **Mode:** {{mode}}{{focus_line}}
- **Schema version:** {{schema_version}}
- **Generated:** {{updated_at}}
- **State file:** `{{state_path}}`
{{git_sha_line}}
## Executive summary

{{exec_summary}}

{{run_log_diff_section}}
## Naive architecture

{{naive_arch_summary}}

**Business context.** {{business_context}}

**Confirmed stack facts.**
{{stack_facts}}

**Assumptions.**
{{assumptions}}

**Components.** {{component_count}} ({{component_kinds}})

**Diagram.** See `architecture_before.mmd`.

```mermaid
{{mermaid_before}}
```

## Stressors

{{stressor_count}} stressors across {{stressor_categories_present}} categories.

{{stressor_table}}

## Attractors and residues

Per-stressor derivation. {{ar_count}} entries.

{{attractor_residue_table}}

## Residue stack

{{residue_stack_count}} deduped residues.

{{residue_stack_section}}

## Contagion

{{contagion_narrative}}

**Hotspots.**
{{hotspots_list}}

**Brittleness rank (top 5).**
{{brittleness_list}}

**Stressor coverage (lowest 5).**
{{coverage_low_list}}

**Orphan residues:** {{orphan_residues}}

**Diagram.** See `architecture_after.mmd`.

```mermaid
{{mermaid_after}}
```

Full coupling matrix: `contagion.csv`.

## Criticality

- **N** = {{N}}
- **K** = {{K}}
- **P** = {{P}}
- **Regime:** {{regime}}

{{deltas_section}}

## Open questions

{{open_questions_list}}

## Appendix

- State file: `{{state_path}}`
- Mermaid before: `{{mermaid_before_path}}`
- Mermaid after: `{{mermaid_after_path}}`
- Contagion CSV: `{{csv_path}}`
- Summary JSON: `{{summary_json_path}}`
