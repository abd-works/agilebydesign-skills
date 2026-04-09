# Inheritance when behavior generalizes — payments example

**Skill:** abd-ooad — **Step 11:** subtype only when **substitutable** behavior differs.

**Upstream:** `turn-verbs-into-operations.md`.

> **Continual refinement:** Full notation is in **[Domain model Markdown](../library/domain-model.md)** (*Domain concept* template; class definition and diagram refined together). In this payments thread, **`**newly added**`** marks a property or operation line **first introduced in this step file** (Steps 1–4 stay pre-notation; formal `- <type> property` / `operation(...) → return` lines begin at Step 5).

---

## Candidate hierarchy

**PaymentMethod** (abstract or interface) — **authorize**, **capture**, **supportsPartialCapture** — **if** each rail implements differently **and** callers use polymorphism.

| Subtype | Justified when |
|---------|------------------|
| **CardMethod** | 3DS, network tokens — extra **redirect** flow. |
| **BankTransferMethod** | Different settlement timing; no “capture” in card sense. |
| **WalletMethod** | Balance vs card rails. |

**Avoid** subclass explosion for **every** PSP brand if behavior is **adapter**-level (Stripe vs Adyen) — that’s **composition** (connector), not inheritance from **PaymentMethod**.

---

## Rule of thumb (payments)

- **Inherit** from **PaymentMethod** when **domain** distinguishes **how** the customer pays (card vs bank vs wallet).
- **Compose** **PspConnector** when **infrastructure** differs (same card semantics, different API).

---

## Inheritance decisions → term-registry.md

> Tag notes on the class model with `[s1-p11]` — see `templates/domain model template.md` for the full tag table.

Record subtype decisions and rejected inheritance in `term-registry.md` Notes. Use Notes labels (see **`library/term-capture`** for the full label list).

Common Notes labels added at this phase:

- `Classified - {{kind}} {{reason}}` — when a term is confirmed as a subtype (kind: `Entity`, `Role`, etc.) or ruled out
- `Promoted - {{from_target}} → {{to_target}} {{reason}}` — when a term moves from property to class due to substitutable behavior
- `Tension - **{{TensionName}}** {{what_is_ambiguous_or_conflicting}}` — when it is unclear whether behavioral difference warrants inheritance
- `Follow-up - {{question_or_action}}` — deferred hierarchy decisions

**If callers don't use polymorphism, inheritance is likely wrong — record the tension and keep it flat.**

---

## Carry forward → Step 12

Formalize **abstract class vs interface** for **PaymentMethod** and **ports** for PSP.

---

## Continual refinement (this step)

- **Delta:** **PaymentMethod** family (**CardMethod**, **BankTransferMethod**, **WalletMethod**) as substitutable subtypes — add subtype concept headings per [Domain model Markdown](../library/domain-model.md) (`### **Subtype** : **PaymentMethod**`) with **`**newly added**`** on subtype **operation** lines when first introduced.

---

## Action Checklist

- [ ] Have you applied the "substitute without breaking callers" test before using inheritance?
- [ ] Is each subtype genuinely behaviorally different from its siblings, not just data-different?
- [ ] Have you avoided inheritance where composition would be a cleaner boundary?
- [ ] Have you added subtype concept headings to the spec for every hierarchy introduced?
- [ ] Have you added `Classified` or `Promoted` notes to `term-registry.md` for subtype decisions, and `Tension` notes for any deferred or contested hierarchy choices?
- [ ] Have you noted carry-forward items to Step 12 (abstract classes and interfaces)?

---

## Prompt

> **Validate and fix when you find problems.** This step may surface bloat, unclear boundaries, missing invariants, naming drift, spec conflicts, or other robustness gaps. When you notice any of that in your work, **validate** and **fix** the model (or **map-model-spec.json** / class diagram) **before** moving on; record **explicit debt** only when you cannot fix yet, with a clear follow-up.
