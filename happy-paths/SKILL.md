---
name: happy-paths
description: This skill should be used when the user asks to "document a happy path", "write a happy path for X", "create happy path docs", "capture the ideal user flow", "scaffold happy_paths/", or wants a structured Markdown file describing how a specific user problem is ideally solved end-to-end. Each happy path is one Markdown file in `happy_paths/<slug>.md` in the user's project. Pairs with the `happy-path-test` skill, which executes these files in a browser.
version: 0.1.0
---

# Happy Paths — author the ideal solve for one user problem

A *happy path* is a single Markdown file describing exactly how one user problem is solved when nothing goes wrong. One file = one user goal = one slug. Files live in `happy_paths/<slug>.md` in the user's project root and are read both by humans (as living spec) and by the `happy-path-test` skill (as a test plan).

This skill creates and maintains those files. It does **not** run them — that's `happy-path-test`.

## When to use this skill

**Use it for:**
- Capturing the canonical "do X" flow for a feature so onboarding, QA, and tests can share one source of truth.
- Pinning down requirements during design — what does success actually look like, click by click?
- Scaffolding the `happy_paths/` folder for a new project.
- Updating a happy path after a UI or flow change.

**Do not use it for:**
- Edge cases, failure modes, or negative tests. Those belong in a separate doc, not in `happy_paths/`. A happy path is the *ideal* path; if it forks, it's two happy paths.
- Generic user-journey storytelling without concrete steps and selectors. The output must be testable.
- API contract docs (use OpenAPI/AsyncAPI for those).

## Read this first

Load **`references/format_spec.md`** before writing anything. It defines the exact frontmatter fields and step grammar that `happy-path-test` parses. Drift from the spec breaks the runner.

For a complete worked example, load **`references/examples/login_signup.md`**.

## Core loop

1. **Identify the user problem in one sentence.** Format: "A *<persona>* wants to *<verb>* so they can *<outcome>*". If you can't fit it in one sentence, it's two happy paths.
2. **Pick a slug.** Lowercase, kebab-case, ≤ 40 chars, verb-led. Examples: `signup-with-email`, `checkout-single-item`, `reset-forgotten-password`. See `references/format_spec.md` § Slug rules.
3. **Confirm `happy_paths/` exists in the user's project root.** Create it if not. Write the new file at `happy_paths/<slug>.md`.
4. **Fill the frontmatter.** Required: `slug`, `title`, `user_problem`, `persona`, `preconditions`, `test_data`, `success_criteria`, `out_of_scope`. Optional: `runner_hints`, `tags`. Validate against the spec.
5. **Write the steps.** One numbered Markdown list. Each step is one *observable* action. The grammar is in `references/format_spec.md` § Step grammar — follow it exactly so the parser can read the file.
6. **Sanity-check.**
   - Every step has a selector or a URL or a CLI/API target — never just "the user does X".
   - Every step's expectation is *observable* (text on screen, URL change, status code) — not internal state.
   - `success_criteria` is what the *user* sees, not what the database holds (unless the user has db access).
   - `out_of_scope` lists at least one thing the path deliberately excludes — forces you to scope.
7. **Save and report.** Write to `happy_paths/<slug>.md`. Print a one-line summary: `wrote happy_paths/<slug>.md (N steps, M success criteria)`.

## When to load which reference

| Step | Reference |
|---|---|
| Top of run | `references/format_spec.md` |
| Eliciting the flow from the user | `references/writing_guide.md` |
| First time on a project | `references/examples/login_signup.md` |
| Boilerplate for a new file | `assets/template.md` |

## Output

A single file at `<project-root>/happy_paths/<slug>.md`. Nothing else. No README updates, no test scaffolding — testing is the other skill's job.

## Verification

Reading the file end-to-end, a person who has never used the product should be able to follow the numbered steps and reach the success criteria without asking a clarifying question. If they can't, the file is incomplete.

The `happy-path-test` skill reads the same file and executes it. If the parser there rejects the file, the format_spec was violated — fix it.

## Bundled resources

- `references/format_spec.md` — frontmatter schema + step grammar (canonical).
- `references/writing_guide.md` — interview prompts, common pitfalls, scoping a single user problem.
- `references/examples/login_signup.md` — gold reference end-to-end example.
- `assets/template.md` — empty boilerplate, copy and fill.
