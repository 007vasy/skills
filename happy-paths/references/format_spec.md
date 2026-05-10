# Happy path file — format spec

This is the **canonical** format. The `happy-path-test` skill parses files with this exact shape; any drift breaks execution.

## File location

`<project-root>/happy_paths/<slug>.md`

One file per user problem. No subfolders inside `happy_paths/`. If you have so many that you want to group them, use slug prefixes (`auth-signup-with-email.md`, `auth-reset-password.md`).

## Slug rules

- Lowercase ASCII, kebab-case, `[a-z0-9-]+`.
- Verb-led when possible (`signup-with-email`, not `email-signup`).
- ≤ 40 characters.
- Must equal the `slug:` value in frontmatter and the filename without `.md`.

## Frontmatter

YAML between `---` fences at the top of the file. Required keys are marked **R**.

```yaml
---
slug: signup-with-email                       # R, matches filename
title: New user signs up with email           # R, sentence case
user_problem: A first-time visitor wants to create an account so they can save their work   # R, single sentence
persona: First-time visitor                   # R, short noun phrase
tags: [auth, signup]                          # optional, lowercase, used for filtering in test runner

runner_hints:                                 # optional but strongly recommended
  base_url: https://app.example.com           # used by Playwright/Chrome runner if step targets are relative
  default_runner: playwright                  # one of: playwright, chrome
  viewport: { width: 1280, height: 800 }      # optional
  storage_state: tests/.auth/anonymous.json   # optional, Playwright storage state file

preconditions:                                # R, list of plain-English statements (must all be true before step 1)
  - The user has a valid email inbox they can read
  - No account exists for that email
  - The signup feature flag is on for the test tenant

test_data:                                    # R, key/value map of concrete inputs the steps reference
  email: e2e-{{timestamp}}@example.test       # {{timestamp}}, {{uuid}}, {{random:8}} are runner-substituted
  password: SuperSecret!42
  display_name: Test User

success_criteria:                             # R, list of observable post-conditions
  - User lands on /dashboard
  - A welcome banner shows the display_name from test_data
  - The header shows a "Log out" link

out_of_scope:                                 # R, list of things this happy path does NOT cover (forces scope)
  - Email verification (covered by verify-email-from-inbox.md)
  - SSO / OAuth signup
  - Password reset
---
```

### Validation rules

- `slug` matches the filename.
- `user_problem` is a single sentence ending in a period.
- `preconditions`, `success_criteria`, `out_of_scope` each have at least one entry.
- `test_data` keys are referenced as `{{test_data.<key>}}` in the steps below.
- `runner_hints.base_url`, if set, must be a full URL (`http://` or `https://`).

## Body — sections

The body must contain these sections in this order. Extra sections are allowed at the end.

### `# <title>`

H1. Same as `title:` in frontmatter.

### `## Why this matters`

One paragraph. Business context: who, why now, what value the user gets. Skim-able for a stakeholder.

### `## Steps`

A numbered Markdown list. **Each list item is one observable action.** This is the part the parser reads.

#### Step grammar

Each step starts with a bold action verb, followed by the target. Sub-bullets carry selector and expectation.

```markdown
1. **<Verb>** <target>
   - Selector: <css-or-role-or-text>           (when DOM-targeted)
   - Expect: <observable>                       (assertion the runner verifies after the action)
   - Note: <free text>                          (optional, ignored by runner, kept for humans)
```

Allowed verbs (the parser recognises these — anything else is treated as a free-text step the Chrome runner narrates and Playwright runner skips with a warning):

| Verb | Meaning | Example target |
|---|---|---|
| `Navigate to` | Load a URL | `/signup` or `https://example.com/signup` |
| `Click` | Click an element | `the "Create account" button` |
| `Fill` | Type into an input | `the email field with {{test_data.email}}` |
| `Select` | Pick from a `<select>` or combobox | `country = "Norway"` |
| `Check` / `Uncheck` | Toggle a checkbox | `"I agree to the terms"` |
| `Upload` | File input | `avatar.png to the avatar field` |
| `Press` | Keyboard | `Enter` |
| `Wait for` | Wait for selector / URL / network idle | `selector [data-testid="dashboard"]` or `url contains /dashboard` |
| `Expect` / `Verify` / `Assert` | Pure assertion, no action | `the welcome banner shows {{test_data.display_name}}` |

#### Selector forms (in priority order)

The parser and runners prefer accessible, stable selectors:

1. `role:button[name="Create account"]` — ARIA role + accessible name. **Preferred.**
2. `text:"Create account"` — exact visible text.
3. `[data-testid="signup-submit"]` — explicit test id. Stable but requires a code change to add.
4. `css:.btn.primary` — raw CSS. **Last resort** — fragile.

Mix freely; one form per step. The Chrome runner passes them to `mcp__claude-in-chrome__find`; the Playwright runner maps them to `getByRole`, `getByText`, `locator`, etc.

### `## Success criteria`

Repeats the frontmatter list as a Markdown bullet list, optionally with one-line clarification per criterion. Humans read this section; the runner reads the frontmatter version.

### `## Notes` (optional)

Anything a human reader or test author should know — flakiness traps, environment caveats, links to PRs.

## Anti-patterns the spec exists to prevent

1. **"The user does X."** Vague. Replace with a verb + target + selector + expectation.
2. **Internal-state assertions.** "A row exists in `users` table" — the user can't see that. If the runner has DB access, fine, but call it out and label it `Verify (internal)`.
3. **Conditional branching.** "If the user has 2FA, then…" — that's two happy paths. Split the file.
4. **Free-prose steps with no observable.** Every step needs an `Expect:` *or* must be a side-effect-free `Navigate to`/`Fill` that's verified by the next step.
5. **Made-up selectors.** Don't invent `[data-testid=…]` values that don't exist in the product. Either confirm the selector or use `role:` / `text:` and let the runner figure it out.
6. **Real personal data.** `test_data` should use clearly synthetic emails (`@example.test`), throwaway names. Never paste a real user's email.

## Round-trip with the parser

```bash
python3 ../happy-path-test/scripts/parse_happy_path.py --in happy_paths/<slug>.md --out -
```

A valid file produces a JSON object with `frontmatter` and `steps` keys, no warnings. Warnings indicate spec violations the runner will degrade on.
