---
scanner: test_structure_scanner.py
---

# Rule: Use Thorough E2E Tests

End-to-end tests are **mandatory** for every sub-epic. E2E tests must reuse the base helper class (not be manually written from scratch), verify **logic** (filtering, eligibility, domain rules) not just element presence, and be executed as a final verification step after implementation. E2E tests exercise the same Gherkin scenarios as server and client tests, but through the complete user workflow: browser → React → HTTP → Express → MongoDB → response → rendered UI.

## E2E Tests Require a Running Application

**E2E tests cannot run without a live server.** Generating `*_e2e.spec.ts` files is not sufficient — the project also needs runnable composition roots:

- `packages/app-server/` — Express entry point that mounts domain routes
- `packages/app-client/` — React/Vite shell that renders domain components

Do **not** tell the user they can run `npx playwright test` until both composition roots exist and a dev server is running. Running Playwright against a missing server produces `ERR_CONNECTION_REFUSED` errors on every test — this is a broken state, not a partial one.

**The complete generation order is:**
1. Domain packages (`shared/`, `server/`, `client/`) ← what the domain module template produces
2. Composition roots (`app-server/`, `app-client/`) ← required before E2E tests work
3. `playwright.config.ts` with a `webServer` block so Playwright starts the app automatically

## DO

- Create `*_e2e.spec.ts` for every lowest sub-epic.
- Extend the base helper class for E2E-specific setup (Playwright page, browser context).
- Assert on **domain logic outcomes**: filtered lists exclude ineligible items, tooltips show remaining time, selected recipients persist across navigation.
- Run E2E tests after implementation as final verification.
- Test the same scenarios as server/client tiers, with complete workflow emphasis.

```typescript
// select-recipient_e2e.spec.ts — CORRECT: reuses helper, verifies logic
import { test, expect } from '@playwright/test';
import { SelectRecipientE2EHelper } from './helpers/select-recipient.e2e';

test.describe('View Active Recipients', () => {
  const helper = new SelectRecipientE2EHelper();

  test.beforeEach(async ({ page }) => {
    await helper.setup(page);
  });

  test('user views list of active recipients when initiating wire payment', async () => {
    await helper.givenEnterpriseHasRecipientsWithActiveStatus();
    await helper.whenUserInitiatesWirePayment();
    await helper.thenOnlyActiveRecipientsDisplayed();
    await helper.thenPendingRecipientsAreExcluded();  // verifies logic, not just count
  });

  test('user cannot select pending recipient (MX country variance)', async () => {
    await helper.givenCountryIsMX();
    await helper.givenRecipientCreated15MinutesAgo();
    await helper.whenUserViewsRecipientList();
    await helper.thenRecipientIsNotSelectable();
    await helper.thenTooltipShowsRemainingTime('15 minutes');  // verifies domain logic
  });
});
```

## DON'T

- Skip E2E tests for any sub-epic.
- Write E2E tests that only check element presence without verifying logic.
- Write E2E tests from scratch without reusing the helper class.
- Forget to run E2E tests after implementation.
- Test only the happy path — include edge cases and domain variants.
- Tell the user they can run `npx playwright test` before `app-server/` and `app-client/` are scaffolded — E2E tests require a live server.

```typescript
// WRONG — only checks elements exist, doesn't verify filtering logic
test('recipients page loads', async ({ page }) => {
  await page.goto('/recipients');
  await expect(page.locator('.recipient-card')).toBeVisible();  // WRONG: no logic verified
  // Does NOT check that Pending recipients are excluded
  // Does NOT verify country-specific behavior
});

// WRONG — manually written without helper, duplicates setup logic
test('select recipient', async ({ page }) => {
  await page.goto('/recipients');
  await page.click('[data-testid="recipient-1"]');  // WRONG: hardcoded, no helper
  await expect(page.locator('.selected')).toHaveCount(1);
});
```
