# Residuality Theory — primer

Load this once at the start of any new project. Skip on `iterate` if a state file already exists.

## The one-paragraph version

Most software architecture pretends the future is knowable: gather requirements, design, build, ship. Residuality Theory (Barry O'Reilly) starts from the opposite assumption — that the system you ship will meet stressors nobody listed, including ones nobody could have listed. Instead of trying harder to predict, you stress-test the *naive* architecture against deliberately diverse stressors, observe which **attractors** (stable states the business gets pulled into when the stressor hits) emerge, and add the smallest possible **residues** (architectural changes) that let the system survive each attractor. The collected residues become the real architecture. Then you check the residues against each other — **contagion** analysis — to find the dangerous hidden couplings before they bite.

## Vocabulary

**Naive architecture.** What you would draw on a whiteboard if a non-engineer asked "how does it work?". The pre-stress design. Honest about its assumptions, free of resilience patterns added on reflex.

**Stressor.** Any external event that perturbs the system. Not just outages — also regulatory changes, market shifts, social engineering, cable theft, leap seconds, a key engineer leaving. The point is *diversity* and *unexpectedness*. Stressors come from 9 categories (see `stressor_catalogue.md`).

**Attractor.** Where the business state ends up when the stressor hits and you do nothing. Always described from the *business* side, not the tech side. Not "the database fails" but "we lose every payment that arrived in the last 90 seconds and customers see double-charges".

**Residue.** The smallest architectural change that lets the business survive the attractor. Minimality is non-negotiable. If your residue requires replacing a component, you have written down another attractor by accident — go back. Residues should fit in 1–3 sentences and have an obvious implementation hint.

**Residue stack.** The collection of residues across all stressors, deduped (because one residue often addresses several stressors). The stack *is* the resilient architecture.

**Contagion.** When two residues touch the same component or share a hidden assumption, a stressor that breaks one can cascade into the other. The contagion matrix surfaces these couplings; the brittleness rank surfaces the worst ones.

**Incidence matrix.** Rows are residues, columns are stressors. Cell `(r, s)` = 1 if residue `r` addresses stressor `s`. Used to compute residue load (how many stressors each residue carries) and stressor coverage (how well each stressor is addressed).

**Coupling matrix.** Rows and columns are residues. Cell `(i, j)` is a 0–1 score of how likely residue `i` failing causes residue `j` to fail. Comes from shared components, shared assumptions, and explicit `couplings[]` entries.

**Criticality (NKP).** From Stuart Kauffman's NKP model. **N** = number of components, **K** = average coupling per component, **P** = constraint density. Systems sit on a spectrum: too low K and you are *frozen* (rigid, brittle to novelty); too high K and you are *chaotic* (small perturbations cascade). The desirable band is the **edge of chaos** — high enough K to adapt, low enough to contain failures. See `criticality_guidance.md` for the heuristic.

**Edge of chaos.** The target regime. Adaptive, not catastrophic. Most production systems start *frozen* (too few residues, too tightly coupled to a happy path) and need stressor-driven residues to climb to the edge.

## The loop (canonical, in order)

1. **Capture naive architecture.** Components, edges, business context, assumptions. No resilience theatre. What is *actually* there today (or in the proposal).
2. **Generate stressors.** ≥30, diverse across all 9 categories, including ≥3 black-swan / absurd entries. Hit the floors in `stressor_catalogue.md`.
3. **Per stressor, derive attractor + residue.** Attractor first (business-language description of what happens if you do nothing); then the smallest residue that survives it. Cite a `user_stack_facts` entry the residue is compatible with, or ask the user.
4. **Stack and dedupe.** Many residues collapse together (one circuit breaker often covers 6 different outage stressors). `scripts/residue_dedupe.py` does the merge; the union of `applies_to_stressors` proves coverage.
5. **Contagion analysis.** Build the incidence + coupling matrices, surface hotspots, brittleness rank, orphan residues.
6. **Criticality check.** Estimate N, K, P; label the regime; suggest deltas if frozen or chaotic.
7. **Render report.** Markdown + before/after Mermaid + CSV + JSON summary, with run-log diff if iterating.

## Three rules nobody breaks

1. **Business-first language.** Stressors and attractors are written so a non-engineer can engage. Tech detail goes in residues.
2. **Minimal residues.** Smallest viable change. Library patterns first; novel residues only if no pattern fits and you can justify the cost.
3. **No fictional stack.** Every residue cites at least one `user_stack_facts` entry. If you can't, ask — don't invent.

## Source material

- Barry O'Reilly, *Residues: Time, Change, and Uncertainty in Software Architecture* (Leanpub).
- GOTO Copenhagen 2025 talk — EV charging worked example begins ~29:06; contagion ~38:39.
- Earlier deck with incidence-matrix examples: https://www.jfokus.se/jfokus22-preso/Residuality-Theory.pdf
- Stuart Kauffman's NKP model for criticality intuitions.
