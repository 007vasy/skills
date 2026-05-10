---
slug: signup-with-email
title: New user signs up with email
user_problem: A first-time visitor wants to create an account so they can save their work.
persona: First-time visitor
tags: [auth, signup]

runner_hints:
  base_url: https://app.example.com
  default_runner: playwright
  viewport: { width: 1280, height: 800 }

preconditions:
  - The user has a valid email inbox they can read
  - No account exists for the test email
  - The signup feature flag is on for the test tenant

test_data:
  email: e2e-{{timestamp}}@example.test
  password: SuperSecret!42
  display_name: Test User

success_criteria:
  - User lands on /dashboard
  - The dashboard welcome banner shows the display_name from test_data
  - The header shows a "Log out" link

out_of_scope:
  - Email verification (covered by verify-email-from-inbox.md)
  - SSO / OAuth signup
  - Password reset
  - Onboarding tour after signup (covered by complete-onboarding-tour.md)
---

# New user signs up with email

## Why this matters

Email signup is the cheapest acquisition path and the baseline for every other auth method. If this flow breaks, no new user can reach the product. It also gates downstream funnels (onboarding tour, first project creation), so a regression here is a top-of-funnel incident.

## Steps

1. **Navigate to** `/signup`
   - Expect: page title contains "Sign up"
   - Selector: `role:heading[name="Create your account"]`

2. **Fill** the email field with `{{test_data.email}}`
   - Selector: `role:textbox[name="Email"]`

3. **Fill** the password field with `{{test_data.password}}`
   - Selector: `role:textbox[name="Password"]`

4. **Fill** the display name field with `{{test_data.display_name}}`
   - Selector: `role:textbox[name="Display name"]`

5. **Check** the "I agree to the terms" checkbox
   - Selector: `role:checkbox[name="I agree to the terms"]`

6. **Click** the "Create account" button
   - Selector: `role:button[name="Create account"]`
   - Expect: navigation to URL containing `/dashboard`

7. **Wait for** selector `[data-testid="welcome-banner"]`
   - Expect: element is visible within 5s

8. **Verify** the welcome banner text
   - Selector: `[data-testid="welcome-banner"]`
   - Expect: text contains `{{test_data.display_name}}`

9. **Verify** the header logout link is present
   - Selector: `role:link[name="Log out"]`
   - Expect: element is visible

## Success criteria

- User lands on `/dashboard`.
- The dashboard welcome banner shows the display name they entered.
- The header has a "Log out" link, indicating the session is established.

## Notes

- The signup endpoint uses a 1–2s server-side throttle. The `Wait for` in step 7 is intentional — without it the welcome banner can race the assertion.
- `{{timestamp}}` resolves to a unix-millis integer at run time so the email is unique per run. Re-running the same path twice with the same email would fail precondition 2.
- The "I agree" checkbox in step 5 is required by the form — skipping it leaves the submit button disabled and the test will hang on step 6.
