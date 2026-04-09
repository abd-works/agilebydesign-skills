# Properties and operations — payments example

**Skill:** abd-ooad — matches **Step 6: Properties and operations** in `SKILL.md`.

**Upstream:** `responsibilities-and-collaborators.md` (Step 5), `nouns-verbs-rules-and-states.md`.

Convert the responsibility statements from Step 5 into first-class typed members. **Properties first, then operations that exercise them.** Every property answers: *What must this object know to fulfil its responsibility?* Every operation answers: *What must this object do, and who calls it?*

Use **contextual names** (e.g. `authorizedMoney`/`capturedMoney` instead of a vague `amount` when partial capture matters). A property that keeps recurring across operations is a value object. A verb that belongs to an application service must be moved out now.

---

## Properties

### Payment (aggregate root)

| Property | Why it belongs here |
|----------|---------------------|
| `id` | Identity of this payment attempt. |
| `idempotencyKey` | Correlate retries; enforce "no double success" for same client intent. |
| `orderRef` | **OrderId** (external BC) — links checkout to payment without duplicating cart lines. |
| `payerRef` | **PayerId** — who pays; sanctions check uses context, not a full `Customer` graph. |
| `merchantRef` | **MerchantId** — routing and settlement context. |
| `routing` | **RoutingContext** VO — dimensions that pick connector (currency, region). |
| `presentmentMoney` | **Money** — what the payer authorizes in their currency. |
| `settlementMoney` | **Money** — if different from presentment (global); nullable if same. |
| `feeBreakdown` | **FeeBreakdown** VO — fees shown/charged for this attempt. |
| `fxQuoteRef` | **FxQuoteRef?** — nullable handle for global flows. |
| `methodSelection` | **PaymentMethodSelection** VO — chosen method snapshot (kind + safe metadata). |
| `state` | **PaymentState** — lifecycle position. |
| `authorizedMoney` / `capturedMoney` | **Money** (or single progression) — supports partial capture without a vague `amount`. |
| `midRateSnapshot` | **MidRateSnapshot?** — immutable receipt stamp when legal requires. |
| `connectorRef` | **ConnectorId** — which integration served this attempt. |
| `redirectContext` | **RedirectContext?** VO — return/cancel URLs, PSP session id if 3DS/redirect. |
| `timestamps` | `createdAt`, `authorizedAt?`, `capturedAt?`, `settledAt?`, `failedAt?` |

**Deliberately omitted from Payment:** tax lines, coupon state, cart items (Order/cart BC); full Merchant entity (only ref); PAN/CVV (PSP tokens); frontend string copy (Failure mapping policy).

---

### Refund

| Property | Why it belongs here |
|----------|---------------------|
| `id` | Distinct refund case. |
| `paymentRef` | **PaymentId** — which payment is being reversed. |
| `refundMoney` | **Money** — amount of this refund (partial or full). |
| `reason` | **ReasonCode** — chargeback prep / compliance. |
| `state` | Refund lifecycle: requested → processing → completed / failed. |
| `requestedAt`, `completedAt` | Traceability. |

---

### Dispute (only if aggregate lives in this BC)

| Property | Why |
|----------|-----|
| `id` | Case identity. |
| `paymentRef` / `refundRef` | Links to money movements. |
| `externalCaseId` | PSP or Risk system id. |
| `ownership` | `platform` \| `merchantOfRecord` — data reflecting policy, not decision logic. |
| `state` | Open / won / lost. |

---

### AuditEntry (immutable)

| Property | Why |
|----------|-----|
| `id` | Log line identity. |
| `paymentRef` | Which aggregate. |
| `fromState`, `toState` | Transition. |
| `actor` | **ActorKind** — `system` \| `user` \| `psp_webhook`. |
| `occurredAt` | Ordering. |
| `payloadRef?` | Optional pointer to raw PSP snippet — not full card data. |

---

### Value objects — internal shape

| VO | Key fields |
|----|-----------|
| **Money** | `amount`, `currency` (Currency VO or ISO string with validation) |
| **RoutingContext** | `storefrontCurrency`, `merchantRegion` |
| **FeeBreakdown** | `lines: FeeLine[]` or `total: Money` |
| **PaymentMethodSelection** | `kind: PaymentMethodKind`, `displayLabel`, `last4`, `brand` |
| **IdempotencyKey** | `value: string`, optionally `firstSeenAt` |
| **FxQuoteRef** | `opaqueId: string` |
| **MidRateSnapshot** | `rate`, `pair`, `asOf` |
| **RedirectContext** | `returnUrl`, `cancelUrl`, `pspSessionId` |

---

### Contextual naming

| Vague noun | Tighter name in this context |
|------------|------------------------------|
| Amount | `authorizedMoney`, `capturedMoney`, `refundMoney`, `presentmentMoney` |
| User | `payerRef` / PayerId — role in this flow |

---

## Operations

### Verbs → candidate operations (challenged)

| Verb (from spec) | Who owns it? |
|-------------------|-------------|
| take / charge money | **Payment** — `authorize()`, `capture()` lifecycle. |
| block sanctioned payer | **Policy** (`ComplianceGate`) before UI; **Payment** refuses `initiate` if illegal. |
| pick method / confirm | **Application service** orchestrates UI; `Payment.recordMethodSelection()`, `confirm()` if state on aggregate. |
| open redirect / 3DS | **Application + infra**; domain: `Payment.markAwaitingRedirect()` fact. |
| emit `payment.settled` | `Payment.settle()` or domain event when state hits settled — not Warehouse. |
| refund | `Refund.initiate()` or `Payment.requestRefund` if refunds are always subordinate. |
| expire idempotency key | **Policy/config + time**; Payment rejects replay if key expired. |

---

### Payment operations

- `initiate(idempotencyKey, orderRef, payerRef, merchantRef, routing)` — creates attempt or returns same for key.
- `recordMethodSelection(selection)` — snapshot VO when user picks method.
- `recordFees(feeBreakdown)` — after quote.
- `authorize(AuthorizationResult)` — PSP outcome applied.
- `capture(Money)` — partial or full per rail rules.
- `settle()` — emit domain fact; enforce ordering invariants.
- `fail(FailureKind)` — terminal failure.
- `recordPspCallback(payloadRef)` — transition from webhook via application mapping.

**Not** on Payment: `renderCheckoutPage()` (UI), `callStripeHttp()` (adapter).

---

### Refund operations

- `request(Money, ReasonCode)` — valid vs original captured amounts.
- `complete()` / `fail()` — rail outcomes.

---

### Application / use-case layer

- **Place payment** — coordinates cart lock, Payment aggregate, PSP adapter, redirect URLs.
- **Interpret webhook** — maps to `Payment.record...` commands.

**Challenge:** Does `Payer.pay()` exist? Usually **no** — payer is identity; `InitiatePayment` use case uses Payment factory or repository.

---

## Formal domain model additions (Step 6)

Properties added at this phase (tag `[p6]` in model notes). Operations added at this phase (tag `[p6]` in model notes).

### Payment

```
+ id: UniqueID                                                          (p6)
+ idempotencyKey: String                                                (p6)
+ orderRef: OrderId                                                     (p6)
+ payerRef: PayerId                                                     (p6)
+ merchantRef: MerchantId                                               (p6)
+ routing: RoutingContext                                                (p6)
+ presentmentMoney: Money                                               (p6)
+ settlementMoney: Money                                                (p6)
+ feeBreakdown: FeeBreakdown                                            (p6)
+ state: PaymentState                                                   (p6)
+ authorizedMoney: Money                                                (p6)
+ capturedMoney: Money                                                  (p6)
+ connectorRef: ConnectorId                                             (p6)
+ timestamps: PaymentTimestamps                                         (p6)

+ initiate(IdempotencyKey, OrderId, PayerId, MerchantId, RoutingContext): Payment  (p6)
+ recordMethodSelection(PaymentMethodSelection): void                   (p6)
+ recordFees(FeeBreakdown): void                                        (p6)
+ authorize(AuthorizationResult): void                                  (p6)
+ capture(Money): void                                                  (p6)
+ settle(): void                                                        (p6)
+ fail(FailureKind): void                                               (p6)
+ recordPspCallback(String): void                                       (p6)
```

### Refund

```
+ id: UniqueID                                                          (p6)
+ paymentRef: PaymentId                                                 (p6)
+ refundMoney: Money                                                    (p6)
+ reason: ReasonCode                                                    (p6)
+ state: RefundState                                                    (p6)

+ request(Money, ReasonCode): Refund                                    (p6)
+ complete(): void                                                      (p6)
+ fail(): void                                                          (p6)
```

*(Application-layer use cases stay outside aggregate operation lists; reference them in Interactions on the spec when promoted.)*

---

## Properties and operations → term-registry.md

> Tag notes on the class model with `[p6]` — see `templates/domain model template.md` for the full tag table.

Common Notes labels added at this phase:

- `Classified - Property {{reason}}` — when a noun resolves to a property on a class
- `Classified - Operation {{reason}}` — when a verb is confirmed as a domain operation
- `Promoted - Property → Class {{reason}}` — when a property is promoted to its own class (e.g. `Money` extracted from raw `amount`)
- `Tension - **{{TensionName}}** {{what_is_ambiguous_or_conflicting}}` — when property or operation ownership is unclear
- `Follow-up - {{question_or_action}}` — deferred decisions

**Any new VO, aggregate, or operation introduced in this phase gets a term row (or row update).**

---

## Carry forward to Step 7 (relationships and cardinality)

Add relationships and cardinality between Payment, Refund, Order (ref), external catalogs.

---

## Action Checklist

- [ ] Does every class have typed properties derived from its Step 5 responsibility statement?
- [ ] Is every property semantically tight — does the object need it to fulfil its responsibility?
- [ ] Have you removed properties that are purely UI, infrastructure, or application-layer concerns?
- [ ] Have you mapped each domain verb from Step 1 and Step 5 to an owning class or application service?
- [ ] Have you challenged application-layer verbs — do they belong in a service, not a domain object?
- [ ] Does every surviving operation appear on the class as a formal method signature?
- [ ] Have you updated `term-registry.md` with `Classified`, `Promoted`, and `Tension` notes for this phase?
- [ ] Have you noted carry-forward items to Step 7 (relationships)?

---

## Prompt

> **Validate and fix when you find problems.** This step may surface bloat, unclear boundaries, missing invariants, naming drift, spec conflicts, or other robustness gaps. When you notice any of that in your work, **validate** and **fix** the model before moving on; record **explicit debt** only when you cannot fix yet, with a clear follow-up.
