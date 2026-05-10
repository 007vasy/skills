---
name: happy-path-test
description: This skill should be used when the user asks to "test happy paths", "run the happy path tests", "verify happy_paths/<slug>", "scaffold Playwright tests from happy paths", "drive the browser through the happy path", or wants to execute one or more `happy_paths/*.md` files (authored by the `happy-paths` skill) as live browser interactions. Supports two runners — generated Playwright specs for CI/repeatable runs, and Claude-in-Chrome for interactive one-off verification.
version: 0.1.0
---

# Happy Path Test — execute happy_paths/*.md as live browser tests

This skill reads happy-path Markdown files (created by the `happy-paths` skill) and runs them in a browser. It supports two runners:

| Runner | When | Output |
|---|---|---|
| **Playwright** | CI, repeatable runs, regression suite | Generated `tests/happy-paths/<slug>.spec.ts` files + `npx playwright test` invocation |
| **Claude in Chrome** | Interactive verification, one-off, "does this still work?" | Live browser actions via `mcp__claude-in-chrome__*` tools, narrated in chat, optional GIF |

If the user doesn't specify, prefer Playwright when a `playwright.config.*` exists in the project; otherwise prefer Chrome.

## When to use this skill

**Use it for:**
- Running one or more `happy_paths/<slug>.md` files end-to-end and reporting pass/fail per step.
- Scaffolding Playwright tests so that CI inherits the happy-path coverage automatically.
- Smoke-testing a deployment — pick a few critical happy paths, point the Chrome runner at the URL, watch them go.
- Catching the moment a UI change breaks the documented user flow (the `happy_paths/*.md` is the spec; this skill is the conformance check).

**Do not use it for:**
- Authoring or editing happy paths — that's the `happy-paths` skill. This skill never modifies `happy_paths/*.md`.
- General browser automation that has no corresponding happy path file. If you don't have the .md, write it first.
- Performance, load, or security testing.
- Backend/API contract tests where there's no UI step.

## Read this first

Load **`references/parsing_happy_path.md`** to understand what the parser produces and how each step verb maps to runner actions. The two runner files build on its output:

- **`references/runner_playwright.md`** — Playwright code-gen, selector mapping, run command.
- **`references/runner_claude_chrome.md`** — `mcp__claude-in-chrome__*` tool playbook, dialog avoidance, GIF capture.

Load **`references/report_format.md`** before emitting results so the report shape is consistent.

## Core loop

1. **Discover targets.** From the user's phrasing:
   - A specific slug (`test happy_paths/signup-with-email.md`) → that one file.
   - A glob/tag (`test the auth happy paths`) → all files under `happy_paths/` whose `tags:` include the term.
   - "All" / "everything" → every `happy_paths/*.md` in the project.
   List the targets back to the user before running so they can abort if the set is wrong.

2. **Pick the runner.** From explicit user request, then from `runner_hints.default_runner` in the file's frontmatter, then from project signals (`playwright.config.{ts,js,mjs}` present → Playwright, otherwise Chrome). Confirm the choice in one line before running.

3. **Parse each target.** Run `python3 scripts/parse_happy_path.py --in happy_paths/<slug>.md --out -`. Stop and surface any parser warnings before running — warnings indicate spec violations that will degrade the run.

4. **Substitute test_data placeholders.** `{{timestamp}}` → unix millis at run time. `{{uuid}}` → uuid4. `{{random:N}}` → N hex chars. `{{test_data.<key>}}` → the corresponding value from frontmatter `test_data`. The parser leaves placeholders unresolved; resolve them per run so the runner sees concrete values.

5. **Execute via the chosen runner.**
   - **Playwright path:** generate (or refresh) `tests/happy-paths/<slug>.spec.ts` using `scripts/render_playwright.py`, then run `npx playwright test tests/happy-paths/<slug>.spec.ts --reporter=list`. Capture the run output.
   - **Chrome path:** follow `references/runner_claude_chrome.md` step by step. Call `mcp__claude-in-chrome__tabs_context_mcp` first; create a new tab; for each parsed step, call the mapped tool; assert each `expect`. Optionally record a GIF via `mcp__claude-in-chrome__gif_creator`.

6. **Render the report.** Per `references/report_format.md`. Default location `./.happy-path-test/<run-id>/`. Always emit `report.md` (human-readable) and `report.json` (machine-readable). For Playwright runs, also link the Playwright HTML report path.

7. **Surface failures clearly.** If any step failed, the final chat message must:
   - Name the slug, the step number, the action, and the observable that failed.
   - Quote the actual vs expected if available.
   - Suggest the most likely cause (selector drift, slow network, missing precondition).
   - Never auto-edit the happy path file — that's the human's call.

## When to load which reference

| Step | Reference |
|---|---|
| Top of run | `references/parsing_happy_path.md` |
| Playwright path | `references/runner_playwright.md` |
| Chrome path | `references/runner_claude_chrome.md` |
| Report | `references/report_format.md` |

## Output

Default location `./.happy-path-test/<run-id>/`:

- `report.md` — human-readable summary, one section per slug, step-by-step pass/fail.
- `report.json` — same data as a structured object.
- `runs/<slug>.log` — raw runner output (Playwright's `--reporter=list` text or the Chrome action log).
- `runs/<slug>.gif` *(Chrome only, optional)* — recorded interaction.

For Playwright, generated specs live in the user's project at `tests/happy-paths/<slug>.spec.ts` and persist across runs (they are real test files the user can also run via `npx playwright test`).

## Selector resolution

Both runners receive selectors in the four forms defined by the format spec. Mapping:

| Spec form | Playwright | Claude in Chrome (`find` tool) |
|---|---|---|
| `role:button[name="X"]` | `page.getByRole('button', { name: 'X' })` | accessibility-name search |
| `text:"X"` | `page.getByText('X', { exact: true })` | visible-text search |
| `[data-testid="X"]` | `page.getByTestId('X')` (if configured) or `page.locator('[data-testid="X"]')` | CSS selector |
| `css:.foo` | `page.locator('.foo')` | CSS selector |

Both runners resolve in the same priority order; if `role:` selectors fail, fall back to `text:`, then test-id, then raw CSS. This matches accessibility-first testing best practices.

## Verification

The skill is "working" when, given the gold example at `../happy-paths/references/examples/login_signup.md`:

- The parser emits 9 structured steps with no warnings.
- The Playwright generator produces a syntactically valid `.spec.ts` that includes one `test(...)` call with 9 awaited actions/assertions.
- The Chrome runner narrates each step before executing it, calls one `find` per selector, and surfaces a clear failure if (e.g.) the welcome banner never appears.

If a real run on a real product breaks but the spec/example still parses cleanly, the failure is a real product/regression — not a skill bug.

## Bundled resources

- `references/parsing_happy_path.md` — what `scripts/parse_happy_path.py` produces.
- `references/runner_playwright.md` — Playwright code-gen and run protocol.
- `references/runner_claude_chrome.md` — `mcp__claude-in-chrome__*` playbook.
- `references/report_format.md` — report structure (Markdown + JSON).
- `scripts/parse_happy_path.py` — stdlib-only parser, `.md → JSON`.
- `scripts/render_playwright.py` — stdlib-only generator, parsed JSON → `.spec.ts`.
- `assets/playwright_test.tmpl` — Playwright spec skeleton with `{{placeholder}}` slots.
- `assets/report_template.md` — Markdown report skeleton.
