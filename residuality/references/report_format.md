# Report format

Defines the structure, length budgets, and rules for `report.md` produced by `scripts/report_render.py`. The template lives in `assets/report_template.md`; this file documents what each section must contain and why.

## Section order (fixed)

1. **Header** — project name, mode, focus areas (if any), schema version, generated-at, git sha.
2. **Executive summary** — 3 bullets, max.
3. **Run-log diff** — only if `mode: "iterate"` and history has ≥2 entries.
4. **Naive architecture** — recap + Mermaid `architecture_before.mmd`.
5. **Stressors** — table, grouped by category.
6. **Attractors and residues** — per-stressor table; what the business does, what we add.
7. **Residue stack** — deduped list, each with applies-to coverage and library citations.
8. **Contagion** — 3-bullet narrative + matrix preview + hotspots + brittleness top-5 + Mermaid `architecture_after.mmd` with overlays.
9. **Criticality** — N, K, P, regime, deltas.
10. **Open questions and assumptions** — anything the user must answer.
11. **Appendix** — full state.json path, contagion.csv path, summary.json path.

## Length budgets

- Executive summary: **3 bullets, ≤ 25 words each**. If you can't fit, the analysis is too verbose; prune the stressor / residue lists, not the summary.
- Naive architecture recap: **3-5 sentences** + the Mermaid diagram.
- Stressors table: rows can be long; section narrative ≤ 100 words.
- Attractors and residues table: rows can be long; ≤ 100 words narrative.
- Residue stack: ≤ 1 paragraph per residue (5 sentences max).
- Contagion narrative: **3 bullets, mandatory before the matrix**.
- Criticality: ≤ 150 words.
- Open questions: bullet list; no narrative needed.

## Section content rules

### Executive summary

Format:
- **Most-loaded residue:** `<name>` addresses `<N>` stressors.
- **Most brittle coupling:** `<R_a>` → `<R_b>` (contagion weight `<x>`).
- **Criticality:** `<regime>` (N=`<n>`, K=`<k>`, P=`<p>`).

Under focus, the first bullet leads with the focus framing instead.

### Stressors table

Columns: `id | name | category | novelty | horizon | description`

Group rows by category. Show category counts in subheadings (e.g. `### Adversarial (3)`).

### Attractors and residues table

Columns: `stressor | attractor (1 line) | residue id | residue name | source pattern | est. cost`

If `est. cost == "high"`, append a footnote-style flag: `⚠ high-cost residue — re-check minimality`.

### Residue stack

For each residue:
- Heading: `### R12 — <name>`
- Bullets: intent, minimal change, applies to (list of stressor IDs), stack-fit citations, source pattern (or "novel").
- If part of a merge, add: "Merged from: R03, R09 (similarity 0.82, 0.91)"

**Refuse to render** any residue with empty `applies_to_stressors` (orphan) — replace the section with a `_Orphan residues detected — see contagion.orphan_residues; rerun the dedupe step._` notice.

### Contagion section

**Mandatory 3-bullet narrative FIRST**, then the matrix preview (residue load + coverage), then `hotspots[]`, then `brittleness_rank[]` top 5, then the Mermaid `architecture_after.mmd`.

The full coupling matrix is written to `contagion.csv`; do NOT inline a 25×25 grid in the Markdown.

### Criticality section

Format:
- **N** = `<n>`
- **K** = `<k>` (avg coupling)
- **P** = `<p>` (constraint density)
- **Regime:** `<frozen|edge|chaotic|indeterminate>`

If regime != edge, list `deltas[]` as bullets, each with the action and expected NKP shift.

If regime == "indeterminate", say so plainly with the reason ("only 12 stressors generated; need ≥25").

### Empty sections

If a section has no data (e.g. `attractors_residues` skipped in `contagion-only` mode), print:

> _No data — see workflow step `<N>`._

Do NOT silently fabricate. The empty placeholder is a signal, not a failure.

## Voice

- Direct. Imperative where appropriate. ("The most-loaded residue is X. Investigate before adding load.")
- Business-first. Never "the system" — it's the product, the user, the customer.
- No hedging. ("This residue is brittle" is fine; "this residue could possibly be brittle" is not.)
- No emojis except the warning glyph `⚠` reserved for high-cost residues and brittleness flags.

## Worst-case render

If `state.json` is corrupt or missing required sections, `report_render.py` should produce a minimal report with a single section: "Render failed — state file missing or invalid: `<reason>`". Never produce a beautiful report on top of broken data.
