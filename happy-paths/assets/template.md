---
slug: REPLACE-WITH-SLUG
title: REPLACE WITH SENTENCE-CASE TITLE
user_problem: A REPLACE_PERSONA wants to REPLACE_VERB so they can REPLACE_OUTCOME.
persona: REPLACE_PERSONA
tags: []

runner_hints:
  base_url: https://REPLACE.example.com
  default_runner: playwright

preconditions:
  - REPLACE: e.g. The user is not logged in
  - REPLACE: e.g. The feature flag XYZ is on for the test tenant

test_data:
  REPLACE_KEY: REPLACE_VALUE

success_criteria:
  - REPLACE: e.g. User lands on /<route>
  - REPLACE: e.g. <Element> shows <expected text>

out_of_scope:
  - REPLACE: at least one thing this happy path deliberately does NOT cover
---

# REPLACE WITH SENTENCE-CASE TITLE

## Why this matters

REPLACE: one paragraph. Who, why now, what user value, what business value.

## Steps

1. **Navigate to** `/REPLACE`
   - Selector: `role:heading[name="REPLACE"]`
   - Expect: page is visible

2. **Fill** the REPLACE field with `{{test_data.REPLACE_KEY}}`
   - Selector: `role:textbox[name="REPLACE"]`

3. **Click** the "REPLACE" button
   - Selector: `role:button[name="REPLACE"]`
   - Expect: navigation to URL containing `/REPLACE`

4. **Verify** REPLACE
   - Selector: `[data-testid="REPLACE"]`
   - Expect: text contains `REPLACE`

## Success criteria

- REPLACE
- REPLACE

## Notes

REPLACE or delete this section.
