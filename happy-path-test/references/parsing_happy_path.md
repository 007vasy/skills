# Parsing happy-path Markdown

Both runners (Playwright and Claude in Chrome) consume the JSON produced by `scripts/parse_happy_path.py`. This file documents that JSON contract so both runner files can reference it.

## Invocation

```bash
python3 scripts/parse_happy_path.py --in happy_paths/<slug>.md --out -
```

`--in -` reads from stdin. `--out -` writes to stdout. Exit code is `0` even if warnings are present — read `result.warnings` to gate execution.

## Output shape

```json
{
  "frontmatter": {
    "slug": "signup-with-email",
    "title": "New user signs up with email",
    "user_problem": "A first-time visitor wants to ...",
    "persona": "First-time visitor",
    "tags": ["auth", "signup"],
    "runner_hints": {
      "base_url": "https://app.example.com",
      "default_runner": "playwright",
      "viewport": { "width": 1280, "height": 800 }
    },
    "preconditions": [ "...", "..." ],
    "test_data": { "email": "e2e-{{timestamp}}@example.test", ... },
    "success_criteria": [ "...", "..." ],
    "out_of_scope": [ "...", "..." ]
  },
  "steps": [
    {
      "n": 1,
      "raw": "1. **Navigate to** `/signup`",
      "verb": "Navigate to",
      "action": "navigate",
      "target": "/signup",
      "selector": null,
      "expect": "page title contains \"Sign up\"",
      "value": null,
      "note": null
    }
  ],
  "warnings": []
}
```

### Per-step fields

| Field | Meaning |
|---|---|
| `n` | Step number (from the Markdown numbered list) |
| `raw` | Original Markdown line, useful for error messages |
| `verb` | Verb as written (preserves original casing) |
| `action` | Normalised verb id used by runners |
| `target` | What the action operates on, with verb-specific extraction (see below) |
| `selector` | From the `Selector:` sub-bullet, with backticks stripped |
| `expect` | From the `Expect:`/`Verify:`/`Assert:` sub-bullet, OR from inline assert verbs |
| `value` | Verb-specific value (e.g. text to fill, file to upload, key to press) |
| `note` | From the `Note:` sub-bullet, ignored by runners |

### Action ids

| `action` | Source verbs | `target` | `value` |
|---|---|---|---|
| `navigate` | `Navigate to` | URL | — |
| `click` | `Click` | description of the element | — |
| `fill` | `Fill` | field name (text before " with ") | text after " with " |
| `select` | `Select` | field name (text before "=") | option (text after "=") |
| `check` | `Check` | description | — |
| `uncheck` | `Uncheck` | description | — |
| `upload` | `Upload` | field name (text after " to ") | file path (text before " to ") |
| `press` | `Press` | empty | key |
| `wait_for` | `Wait for` | freeform target description | — |
| `assert` | `Expect`, `Verify`, `Assert` | description (e.g. "the welcome banner text") | — |

### Selector forms

The parser does not interpret selectors — it returns the raw string. Both runners interpret in the priority order from the format spec:

1. `role:button[name="X"]` — accessibility role + name
2. `text:"X"` — exact visible text
3. `[data-testid="X"]` or any `[attr="..."]` — attribute selector
4. `css:.foo` (or anything else) — raw CSS

When the prefix is missing, the runners infer from the shape: starts with `role:` → role; starts with `text:` → text; starts with `[` → attribute; everything else → CSS.

## Placeholder substitution

The parser does **not** substitute `{{...}}` placeholders — it leaves them in `value`, `target`, `expect` etc. so runners can substitute per run.

Substitutions both runners must perform:

| Placeholder | Substituted value |
|---|---|
| `{{timestamp}}` | unix milliseconds at run start, as a string |
| `{{uuid}}` | random uuid4 |
| `{{random:N}}` | N hex chars (1 ≤ N ≤ 64) |
| `{{test_data.<key>}}` | `frontmatter.test_data[<key>]` |

Substitute consistently per step — the same `{{timestamp}}` resolves to the same value across all steps in one run.

## Warnings

Warnings are non-fatal but should be surfaced to the user *before* running:

- `Frontmatter missing required key: <X>` — file is incomplete; runner may fail.
- `Slug "<X>" violates [a-z0-9-]{1,40}` — file may not be discoverable consistently.
- `Step N: unknown verb "X"` — runner will best-effort the action; expect failure for that step.
- `Step N: action "X" has no Selector — runner will guess` — likely fragile; ask the author to add a `Selector:` sub-bullet.
- `No '## Steps' section found` — fatal in practice; nothing to run.

If `len(warnings) > 0`, print them and ask the user whether to proceed. Don't auto-proceed when the warnings include "fatal in practice" cases (no Steps section, no required frontmatter).
