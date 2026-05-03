# Workflow — `wizard` mode

Triggered when the user says "walk me through", "interview me", "wizard mode", "I don't know my architecture yet", or otherwise signals they want an interactive build-up rather than a one-shot analysis.

## Pacing rules

- **≤3 questions per turn.** Always. If you have 6 things to ask, ask the most-blocking 3 now and the rest after the user responds.
- After every turn, re-render the partial `naive_architecture` and `user_stack_facts` so the user sees what you have learned. Use a small inline JSON or compact bullet list, not the full state file.
- Confirm before moving on: "Anything missing or wrong before we move to stressors?"

## Question buckets, in priority order

Apply **Block I** from `prompt_templates.md`. The buckets are:

1. **Business context.** Who uses this, what for, what is the moment of value? (1-2 questions)
2. **Happy path.** Walk me through one successful end-to-end interaction. (1 question, often answered in a paragraph)
3. **Components and edges.** What does each step actually call? (multiple turns, ≤3 questions per turn)
4. **The stack.** Datastores, message brokers, clouds, third parties. (1-2 questions per turn until `user_stack_facts[]` has ≥3 entries)
5. **Constraints.** Regulators, latency budgets, cost ceilings, geography. (1-2 questions)
6. **Pains.** "What scares you about this system at 3 a.m.?" (1 question — feeds future stressor brainstorm)

## Ready to advance to `analyze`?

Move from wizard capture into the `analyze` workflow only when ALL of these are true:

- Every component has `name` and `kind`.
- Every edge has `from`, `to`, `kind`.
- `user_stack_facts[]` has ≥3 confirmed entries (not assumed — confirmed by the user).
- `business_context` is non-empty.
- The user has explicitly confirmed: "yes, that's right, let's continue".

When advancing, hand off to **`workflow_analyze.md`** starting at step 4 (stressor generation). Steps 1-3 are already complete.

## When the user gets impatient

If the user says "skip the questions, just do it", switch to `analyze` mode immediately with whatever has been captured. Add an `open_questions[]` entry for each bucket that was skipped, and surface them at the end of the report.

## When the user gets stuck

If the user can't answer a question (e.g. "I don't know what message broker we use"), do not guess. Add it to `open_questions[]` and move on. Residue derivation later will refuse to invent the missing piece — it will surface the gap as a request to the user.
