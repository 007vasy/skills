# Report format

Both runners emit the same shape of report. Default location: `./.happy-path-test/<run-id>/`, where `<run-id>` is `YYYY-MM-DD_HHMMSS`.

## Files

```
.happy-path-test/<run-id>/
├── report.md             # Human-facing summary
├── report.json           # Machine-readable; same data
└── runs/
    ├── <slug-1>.log      # Raw runner output (Playwright stdout, or Chrome action log)
    ├── <slug-1>.gif      # Optional, Chrome only
    ├── <slug-2>.log
    └── ...
```

## `report.json` schema

```json
{
  "run_id": "2026-05-11_140530",
  "started_at": "2026-05-11T14:05:30Z",
  "finished_at": "2026-05-11T14:06:12Z",
  "runner": "playwright" | "chrome",
  "totals": {
    "slugs": 3,
    "passed": 2,
    "failed": 1,
    "skipped": 0
  },
  "results": [
    {
      "slug": "signup-with-email",
      "title": "New user signs up with email",
      "source_path": "happy_paths/signup-with-email.md",
      "status": "pass" | "fail" | "skip",
      "duration_ms": 4321,
      "steps": [
        {
          "n": 1,
          "action": "navigate",
          "target": "/signup",
          "status": "pass",
          "actual": null,
          "expected": null,
          "note": null
        },
        {
          "n": 6,
          "action": "click",
          "target": "the \"Create account\" button",
          "status": "fail",
          "actual": "page url is /signup?error=email-taken",
          "expected": "URL contains /dashboard",
          "note": "Pre-existing account for the test email; check precondition 2"
        }
      ],
      "warnings": [ "..." ],
      "log_path": "runs/signup-with-email.log",
      "gif_path": null
    }
  ]
}
```

## `report.md` shape (use `assets/report_template.md`)

```markdown
# Happy path test run — {{run_id}}

**Runner:** {{runner}}  •  **Duration:** {{duration_s}}s  •  **{{passed}}/{{total}} passed**

## Summary

| Slug | Status | Steps | Duration |
|---|---|---|---|
| signup-with-email | ✅ pass | 9/9 | 4.3s |
| reset-password | ✅ pass | 7/7 | 3.1s |
| checkout-single-item | ❌ fail | 5/8 | 2.9s |

## Failures

### checkout-single-item — step 6: Click "Pay now" button

- **Expected:** navigation to `/order/confirmation`
- **Actual:** page stays on `/checkout`, console shows `[stripe] declined`
- **Likely cause:** test card declined — check `test_data.card_number`
- **Source:** `happy_paths/checkout-single-item.md` line 24
- **Log:** `runs/checkout-single-item.log`

## Per-slug detail

### signup-with-email
... (collapsible per-step list)

### reset-password
...

### checkout-single-item
...
```

## Rendering rules

1. **Lead with totals.** The first paragraph must say `N/M passed`. A reader who only reads the first line should know whether to panic.
2. **Failures section before per-slug detail.** Failure triage is the most-read section; put it where the eye lands.
3. **For each failure, surface four things:** expected, actual, likely cause, source line. Without all four the failure is not actionable.
4. **Do not auto-suggest a code or `.md` fix.** Surface the data; let the human decide. The runner can be wrong about the cause — be explicit ("most likely cause: …; could also be …").
5. **Never fabricate `actual:`** If the runner couldn't read the page state, say so: `actual: <unable to read — page closed before assertion>`.
6. **Console + network excerpts** go in the per-slug detail, not in the failures summary, unless they're the smoking gun.

## Status semantics

- `pass` — runner executed the step and the expectation matched (or the step had no expectation).
- `fail` — runner executed the step but the expectation didn't match, OR the action threw.
- `skip` — step was skipped because an earlier step in the same slug failed and aborted the run, OR because the step's verb was unknown.
- A slug's overall status is `pass` only if every step is `pass`. Any `fail` makes the slug `fail`. All-`skip` is also `fail` (nothing was actually verified).

## Re-runs

Each run gets its own folder; previous runs are not overwritten. The user can `diff` two `report.json` files to see what changed.

For Playwright, the generated `.spec.ts` files are *not* per-run artifacts — they live in the user's repo at `tests/happy-paths/<slug>.spec.ts` and are overwritten on each generation. The Playwright HTML reporter (`playwright-report/`) is also project-level, not per-run-id; link to it from `report.md` rather than copying it.
