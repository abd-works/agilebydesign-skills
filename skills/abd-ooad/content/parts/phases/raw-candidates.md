# Raw candidates

**Skill:** abd-ooad — **Phase-id:** `raw-candidates` (follows `nouns-verbs-rules-and-states`; precedes `thing-vs-data-about-a-thing`).

**What this phase does:** Take the **nouns already extracted** in `nouns-verbs-rules-and-states` and assign each one a **provisional model target** — `Entity`, `ValueObject`, `Enum`, `Policy`, `Role`, `Event`, or `Process` — then add a model stub and a `Classified` note in `term-registry.md`. Record tensions where the right kind is unclear.

**Focus:** Every noun gets a provisional kind and lands in the model. Classifications are confirmed or demoted in the next phase (`thing-vs-data-about-a-thing`).

---

## What you produce

For each noun term from `term-registry.md`, update its **Target** column with the provisional kind and add a `Provisionally Classified` note. Add a `Name << kind? >>` stub to `domain-model.md` under the correct anchor module — the `?` inside the stereotype means provisionally assigned; `thing-vs-data-about-a-thing` (p4) drops the `?` to confirm or changes the kind to demote. Add `Tension` notes for anything with an unclear boundary.

No separate bucket table or list file is created. When the project keeps a class diagram for the slice, update it after the markdown matches (**visual twin**).

---

## Illustrative shape

Taking nouns from `nouns-verbs-rules-and-states`, assign provisional kinds:

| Term (from registry) | Model stub | Notes |
|---|---|---|
| Character, Check | `Character << Entity? >>` | May merge later. |
| DC, bonus | `DC << ValueObject? >>` | VO / enum / struct. |
| roll → resolve | `roll << Process? >>` | End-to-end flow. |
| stacking, advantage | `stacking << Policy? >>` | Modifiers / eligibility. |
| player, GM | `player << Role? >>` | Often actors, not classes. |
| "Check resolved" | `CheckResolved << Event? >>` | If replay / audit matters. |

Each row: update `term-registry.md` Target + add `Classified` note; add `### Name : << kind >>` stub to `domain-model.md`.

**All classifications and tensions go into `term-registry.md`** — not only in the model stubs. Tag model notes with `[p3]` — see `templates/domain model template.md` for the full tag table. See `library/term-capture` for the full Notes label list.

Common Notes labels added at this phase:

- `Provisionally Classified - {{kind}}? {{reason}}` — kind is `Entity?`, `ValueObject?`, `Enum?`, `Policy?`, `Role?`, `Event?`, `Process?`
- `Tension - **{{TensionName}}** {{what_is_ambiguous_or_conflicting}}` — boundaries between kinds
- `Follow-up - {{question_or_action}}` — anything deferred to `thing-vs-data-about-a-thing`

---

## Action Checklist

- [ ] Every noun from `nouns-verbs-rules-and-states` has a provisional Target in `term-registry.md`.
- [ ] Each term has a `Provisionally Classified` note in `term-registry.md`.
- [ ] Each term appears as a `### Name : << kind >>` stub in `domain-model.md` under the correct anchor module.
- [ ] Tensions recorded as `Tension` notes; unclear boundaries flagged for `thing-vs-data-about-a-thing`.
- [ ] No duplicate tables — the model and registry are the single source of truth.

---

## Prompt

> For each noun in the registry: assign a provisional kind, add the model stub, record why. When kind is unclear, name the tension — don't skip it.
