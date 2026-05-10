# Writing guide — eliciting and shaping a happy path

How to take a vague feature request and turn it into a tight, testable happy path file.

## Interview prompts (use when the user is starting from scratch)

Ask in order. ≤ 2 questions per turn.

1. **Who is the user, and what do they want?** Force the format: "A *<persona>* wants to *<verb>* so they can *<outcome>*."
2. **Where do they start?** A URL, a logged-in dashboard, an email link, a deep link from a partner site.
3. **What does success look like — to them?** A confirmation screen, an email, a downloaded file, a row appearing in their inbox. Must be visible to the user.
4. **What's deliberately not in this flow?** Force them to name at least one thing — payment, email verification, multi-currency, mobile, etc.
5. **What test data do we use?** Email, password, names, IDs. Synthetic only.
6. **What flakiness traps do you already know about?** Async waits, auth tokens, cookie banners, 3rd-party iframes.

If the user can't answer (3) or (4), they're not ready — the feature isn't designed enough yet. Pause and surface that.

## Scoping rule: one user, one outcome

If the answer to "what does success look like" has the word **and**, you probably have two happy paths.

| Feels like one path | Actually two |
|---|---|
| "Sign up and verify their email" | `signup-with-email.md` + `verify-email-from-inbox.md` |
| "Add to cart and check out" | `add-to-cart.md` + `checkout-single-item.md` |
| "Upload a file and share the link" | `upload-file.md` + `share-uploaded-file.md` |

Splitting forces each path to be cheap to test in isolation. The cost is composition — the test runner can chain them via `preconditions` ("The user has just completed `signup-with-email`").

## Step-writing checklist

For each step you draft, run this checklist:

- [ ] Does it start with one of the allowed verbs (`Navigate to`, `Click`, `Fill`, `Select`, `Check`, `Uncheck`, `Upload`, `Press`, `Wait for`, `Expect`, `Verify`, `Assert`)?
- [ ] Is the target unambiguous? A single button, a single field, a single URL.
- [ ] Is there a `Selector:` line — preferring `role:`, then `text:`, then `[data-testid]`, then raw CSS?
- [ ] Is there an `Expect:` line — or is this step verified by the next step's `Expect:`?
- [ ] Is the assertion *observable* (visible text, URL, status code) — not internal state?
- [ ] Does it use `{{test_data.<key>}}` rather than inline literals when reusing values?

If a step fails any of these, rewrite before moving on.

## Common pitfalls

### The compound step

> 4. **Fill** the form and click submit.

Two actions. Split:

> 4. **Fill** the email field with `{{test_data.email}}`
> 5. **Click** the "Submit" button

### The intent-as-assertion

> Expect: the user feels welcomed.

Not observable. Replace with:

> Expect: the page shows "Welcome, {{test_data.display_name}}"

### The made-up selector

If you don't know whether `[data-testid="signup-submit"]` exists, don't write it. Use `role:button[name="Create account"]` or `text:"Create account"` — the runner can find those without product-side changes.

### The hidden precondition

> 1. **Navigate to** `/dashboard`

…but the user must be logged in first. Either:
- Add the precondition to frontmatter (`The user is logged in as a free-tier account`), or
- Add a setup step at the top: `1. **Navigate to** /login` etc.

The frontmatter form is preferred — keeps the path focused on the *new* behaviour, not boilerplate. Test runners can compose: log-in setup is its own happy path that this one's `preconditions` references by slug.

### The infinite happy path

If your numbered list has more than ~15 steps, you probably have a journey, not a path. Either split, or accept that this is a long flow and add a `## Notes` section explaining why.

## Iterating on an existing file

When updating after a UI change:

1. Diff the live UI against the file.
2. Update only the steps that changed. Keep step numbers if possible (insert as `4a` rather than renumbering).
3. If frontmatter `success_criteria` changes, that's a behavioural change — flag it in the PR description, since it changes what tests assert.
4. If the change makes the file fork (two outcomes from one starting point), split into two files instead of branching the steps.

## Reviewing someone else's happy path

Read top to bottom *as if you were the runner*. At each step, ask: "Could I do this without asking a clarifying question?" If no, the step needs more detail. If you have to skim or skip, the path is too long.
