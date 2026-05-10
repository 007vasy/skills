# Claude in Chrome runner

Use this runner for interactive verification, one-off "does this still work?" checks, exploratory smoke tests, or when no Playwright config exists in the project. Runs via the `mcp__claude-in-chrome__*` tools — driving a real Chrome window the user can watch.

## Pre-flight (always do this once per run)

Per the global `claude-in-chrome` MCP guidance, **load the Chrome tool schemas before calling them**. At minimum:

```
ToolSearch select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__find,mcp__claude-in-chrome__form_input,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__read_console_messages,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__gif_creator
```

Then:

1. Call `mcp__claude-in-chrome__tabs_context_mcp` to inventory existing tabs. **Never reuse a tab id from a prior session.**
2. Create a fresh tab with `mcp__claude-in-chrome__tabs_create_mcp` (`url` = `runner_hints.base_url` + first step's relative path, or just `about:blank`).
3. If the user wants a recording, start `mcp__claude-in-chrome__gif_creator` with a meaningful filename like `<slug>_run_<timestamp>.gif`. Capture extra frames before and after each interaction.

## Step → tool mapping

| Action | Chrome tool call |
|---|---|
| `navigate` | `mcp__claude-in-chrome__navigate` with `tab_id` and the resolved URL (absolute, or `runner_hints.base_url` + relative target) |
| `click` | `mcp__claude-in-chrome__find` with the selector to confirm presence, then click via the same `find`/`computer` tooling per the tool schema |
| `fill` | `mcp__claude-in-chrome__form_input` with the resolved selector and the substituted value |
| `select` | `mcp__claude-in-chrome__form_input` (for `<select>` inputs the same form_input tool handles options) |
| `check` / `uncheck` | `mcp__claude-in-chrome__find` to locate, then click — confirm checked state with `mcp__claude-in-chrome__javascript_tool` if needed |
| `upload` | `mcp__claude-in-chrome__file_upload` with the resolved file path and selector |
| `press` | `mcp__claude-in-chrome__shortcuts_execute` for named keys, or `mcp__claude-in-chrome__computer` for raw key events |
| `wait_for` | `mcp__claude-in-chrome__find` with retry until the selector resolves; for URL waits use `mcp__claude-in-chrome__tabs_context_mcp` polling |
| `assert` | `mcp__claude-in-chrome__find` (selector visible?) + `mcp__claude-in-chrome__get_page_text` (does it contain the expected string?) |

## Selector resolution

The Chrome `find` tool accepts CSS selectors and accessibility queries. Resolve in priority order:

1. **`role:button[name="X"]`** → if the find tool supports ARIA queries directly, pass it; otherwise fall through to text.
2. **`text:"X"`** → search visible page text via `get_page_text` and locate the element wrapping the match.
3. **`[data-testid="X"]`** or other attribute selectors → pass directly to `find` as CSS.
4. **`css:.foo`** → strip `css:`, pass remainder to `find`.

If a selector can't be resolved after 2 retries with a 500ms delay, mark the step **failed** with reason `selector unresolved: <selector>` and continue to the next step *only if* it's recoverable (no dependency on this step's output).

## Per-step protocol

For every parsed step:

1. **Narrate.** Write a one-line user-facing message: `step <n>/<total>: <verb> <target>`. The user is watching — they need to see what's about to happen.
2. **Substitute.** Resolve `{{timestamp}}`, `{{uuid}}`, `{{random:N}}`, `{{test_data.<key>}}` inside `target`, `value`, `expect`, and `selector`.
3. **Execute.** Call the mapped tool with the substituted values.
4. **Assert.** If the step has an `expect`, verify it. For visible-text expectations, use `get_page_text` + substring check. For URL expectations, read the tab url from `tabs_context_mcp`.
5. **Record.** Append `{n, action, status: pass|fail, note}` to the step log.

If a step fails, decide whether to abort or continue:

- **Abort** when the failed step is a precondition for later steps (e.g. `Click submit` failed → there's no point asserting the next page).
- **Continue** when the failed step is purely an assertion and later steps don't depend on its side effect.

State the decision in the chat ("step 6 failed; aborting because step 7 depends on the navigation it triggers").

## Dialog avoidance

Per the global Chrome tool guidance: **never trigger `alert`, `confirm`, `prompt`, or other modal dialogs.** They block all subsequent tool calls.

If a happy path step would click a button that triggers a confirm dialog (like a destructive "Delete" action), pause and warn the user before executing — they may need to confirm in person, or the page may need to be modified to skip the confirm in test mode.

If you accidentally trigger a dialog and the runner stops responding, instruct the user: *"A modal dialog is blocking further actions — please dismiss it in the browser, then I'll resume from step <n>."*

## Console + network for debugging

When a step fails or behaves oddly:

- `mcp__claude-in-chrome__read_console_messages` with a `pattern` regex matching the slug or app prefix (`[<app>]`) to surface relevant logs without flooding the chat.
- `mcp__claude-in-chrome__read_network_requests` to inspect the failing request (status code, response body) when an assertion expected a server-driven UI change.

Don't paste full console logs into the chat — quote the line numbers + relevant matches.

## Rabbit-hole guard

Per the global Chrome tool guidance:

- After 2-3 failed attempts on the *same* step, stop. Do not keep retrying.
- Report what was attempted and what the page actually shows (via `get_page_text` excerpt).
- Ask the user how to proceed.

The happy path is supposed to be the *easy* path. If it's not working, that's the signal — don't paper over it with retries.

## Cleanup

After the run:

1. Stop GIF capture (if started) and surface the file path.
2. Close the test tab via `mcp__claude-in-chrome__tabs_close_mcp` *unless* the user asked to keep it open for inspection.
3. Emit the report per `references/report_format.md`.

## Caveats

- The Chrome runner is **not** suitable for CI (it requires the user's local Chrome + the MCP extension running). Steer CI use cases to the Playwright runner.
- Browser timing is real wall-clock; very fast assertions can race the page render. Insert `Wait for selector ...` steps in the `.md` if you see flake — don't add silent sleeps in the runner.
- Personal data on the page (cookies, autofilled emails) can leak into the GIF. Warn the user before recording in any environment that's not a clean profile.
