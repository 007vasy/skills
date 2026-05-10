# Playwright runner

Use this runner when the user wants repeatable, CI-friendly tests, or when the project already has `playwright.config.{ts,js,mjs}`.

## Pipeline

```
happy_paths/<slug>.md
   │
   ├─ python3 scripts/parse_happy_path.py      → parsed.json
   │
   └─ python3 scripts/render_playwright.py     → tests/happy-paths/<slug>.spec.ts
       │
       └─ npx playwright test tests/happy-paths/<slug>.spec.ts --reporter=list
```

The generated `.spec.ts` is checked into the user's repo. Re-running this runner against an unchanged `.md` produces a byte-identical spec (modulo the `Generated at:` header timestamp); the regeneration is idempotent. CI can run the spec independently with vanilla `npx playwright test` — no skill required at run time.

## Setup checks (run once per project)

Before generating, verify:

1. `package.json` exists and contains `@playwright/test` in `dependencies` or `devDependencies`. If not, ask the user before installing — adding a dep is a project-level decision.
2. `playwright.config.{ts,js,mjs}` exists. If not, run `npx playwright install` (after asking) — it scaffolds config + installs browsers.
3. The user's project has a `tests/` directory or accepts the convention.

If any check fails, surface it to the user before generating. Don't auto-install browsers (they're hundreds of MB).

## Generation

For each target slug:

```bash
python3 scripts/parse_happy_path.py --in happy_paths/<slug>.md --out /tmp/parsed.json
python3 scripts/render_playwright.py --in /tmp/parsed.json --source happy_paths/<slug>.md --out tests/happy-paths/<slug>.spec.ts
```

The generated file embeds:
- `BASE_URL` from `runner_hints.base_url` (used by `Navigate to <relative>` steps).
- `TEST_DATA` from frontmatter `test_data`, with `{{timestamp}}`, `{{uuid}}`, `{{random:N}}` substituted at run time inside the spec itself.
- A `selectorToLocator(page, raw)` helper that maps the four selector forms (`role:`, `text:`, `[attr=...]`, `css:`) to the right Playwright locator API.
- One `test('...', async ({ page }) => { ... })` block with the parsed steps inlined as `await` calls.

## Selector → Playwright mapping

| Spec form | Generated code |
|---|---|
| `role:button[name="Create account"]` | `page.getByRole('button', { name: 'Create account' })` |
| `text:"Sign up"` | `page.getByText('Sign up', { exact: true })` |
| `[data-testid="signup-submit"]` | `page.locator('[data-testid="signup-submit"]')` |
| `css:.btn.primary` | `page.locator('.btn.primary')` |

## Step → Playwright mapping (highlights)

| Action | Generated |
|---|---|
| `navigate` | `await page.goto(\`${BASE_URL}/<path>\`)` (or absolute URL as-is) |
| `click` | `await selectorToLocator(page, sel).click()` |
| `fill` | `await selectorToLocator(page, sel).fill(value)` (with `subst()` if value contains `{{...}}`) |
| `select` | `await selectorToLocator(page, sel).selectOption(value)` |
| `check` / `uncheck` | `.check()` / `.uncheck()` |
| `upload` | `.setInputFiles(value)` |
| `press` | `await page.keyboard.press(key)` |
| `wait_for` | `selector X` → `selectorToLocator(...).waitFor({ state: 'visible' })`; `url contains X` → `await page.waitForURL(/.../)`; `network idle` → `waitForLoadState('networkidle')` |
| `assert` | `selector + "contains X"` → `toContainText(X)`; `selector + "visible"` → `toBeVisible()`; `url contains X` → `toHaveURL(/.../)` |

For action-bearing verbs that also have an `Expect:` sub-bullet, the renderer emits both — e.g. `Click ... Expect: navigation to URL containing /dashboard` produces a `.click()` *and* a `await expect(page).toHaveURL(/\/dashboard/)`.

Anything the renderer can't classify becomes a `// TODO:` line. Treat those as failing tests until a human edits the `.md` to clarify.

## Running

```bash
npx playwright test tests/happy-paths/<slug>.spec.ts --reporter=list
```

Multi-slug runs:

```bash
npx playwright test tests/happy-paths/ --reporter=list
```

Capture the stdout — it goes into `runs/<slug>.log` and the parsed pass/fail goes into `report.json` per `references/report_format.md`.

## Iteration loop

When a happy path file changes:

1. Re-parse and re-render — the `.spec.ts` will be regenerated.
2. Diff the regenerated `.spec.ts` against the working tree's prior version. The user owns this diff; it's a real source-controlled file.
3. Run the spec.
4. If a step fails, never auto-edit either the `.spec.ts` or the `.md`. Surface the failure with the parsed step number, the selector that didn't resolve, and the user's most recent edits to the `.md` (if you can determine them via `git log -1`). The human decides whether the product or the spec is wrong.

## Caveats

- The generated spec uses `crypto.getRandomValues` and `crypto.randomUUID`, which require Node 18+ or the `crypto` global. Playwright's bundled Node ships them, but if the user runs the spec under an older Node, instruct them to import `node:crypto`.
- `BASE_URL` is read from frontmatter at generation time, not run time. If the URL changes per environment, the user should override via `playwright.config.ts`'s `use.baseURL` and remove the `BASE_URL` constant from the spec by editing the `.md` to drop `runner_hints.base_url`.
- Storage state (`runner_hints.storage_state`) is currently a frontmatter hint only — the generator does not wire it. Doing so would require knowing the project's auth fixture; surface to the user as an optional follow-up: "I see `storage_state: tests/.auth/anonymous.json` in the frontmatter — want me to add `test.use({ storageState: ... })` to the generated spec?"
