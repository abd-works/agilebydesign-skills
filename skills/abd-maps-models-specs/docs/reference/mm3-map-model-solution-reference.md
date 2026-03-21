# MM3 map / model / spec — solution reference (human / offline only)

**This file is not read by the automated builder, orchestrator, or default evaluator.**  
It records an OO analysis & design view for **humans** comparing outcomes. The **automated** evaluator scores **`rules/mm3_domain_critic.json`** against the **Heroes Handbook corpus** (first principles), not this document.

---

# MM3 map / model / spec — object-oriented analysis & design (foundation)

This document is the **promoted domain view** for the MM3 Heroes Handbook fixture: resolution mechanics, character capabilities, powers, and modifiers. It is **not** a mirror of the book’s table of contents; **section titles are navigation**, not a type taxonomy.

---

## 1. Bounded context

| Context | Responsibility | Out of scope here |
|--------|----------------|-------------------|
| **Resolution** | How checks are formed, rolled, and compared to DCs or opposed values | Full combat action economy, initiative detail |
| **Character capabilities** | Durable bonuses and ratings that **participate in checks** (traits, defenses, skills, abilities) | Full character sheet UI |
| **Power construction** | Ranked abilities built from **Effects** with **extras** and **flaws** | Every power name in the book |
| **Modifiers** | Cross-cutting adjustments that attach to effects or powers | Publishing layout, art |

---

## 2. Core abstractions (OOA — responsibilities)

### 2.1 Resolution family — `Check` and specializations

**`Check`** is the abstract **resolution transaction**: inputs (bonuses, circumstances), die mechanics, and outcome vs a target (DC, opposed roll, or resistance).

| Type | Responsibility | Typical collaborators |
|------|----------------|------------------------|
| **Check** | Define the resolution pattern (roll, compare, degree) | Modifier, Trait (for bonuses) |
| **SkillCheck** | Routine or contested use of a **Skill** | Skill, DC |
| **AbilityCheck** | Straight **Ability** vs DC | Ability |
| **AttackCheck** | Roll to hit a target defense | AttackEffect (indirect), Defense |
| **DefenseCheck** | Passive or active defense value used as target | Defense |
| **OpposedCheck** | Two active rolls compared | Check, Trait |
| **ResistanceCheck** | Save vs an effect (e.g. Affliction) | Affliction, Stamina |

*Design rule:* specialization is justified when **substitution** matters for how the check is built and compared—not when only the label changes.

### 2.2 Durable capabilities — `Trait` and roles

**`Trait`** is the generalization for **persistent** character features that grant **bonuses**, **ranks**, or **defense values** used in checks. Not every game noun is a Trait.

| Type | Responsibility | Notes |
|------|------------------|--------|
| **Skill** | Trained capability; bonus to relevant SkillChecks | Often paired with ability default |
| **Ability** | One of the six (or derived) scores; fuels AbilityChecks and some defaults | |
| **Defense** | Target number for attacks (e.g. Parry, Dodge, Fortitude) | Distinct from a one-off bonus |
| **Stamina** | Resource that can interact with fatigue, effort, or resistance paths | Aligns with “toughness / stamina” style resistance in corpus |

**`Power`** is **not** a Trait: it is a **container** for ranked **Effects** and their extras/flaws.

### 2.3 Powers vs effects — composition, not inheritance

| Type | Responsibility |
|------|----------------|
| **Power** | Named, ranked construct; **aggregates** one or more **Effect** instances; selects extras/flaws |
| **Effect** | Atomic mechanical unit (sensory, movement, damage, …); **applied** by a Power or environment |

**Anti-pattern (explicit):** `Power` does **not** extend `Effect`. Powers **have** effects.

### 2.4 Attack-style effects

| Type | Responsibility |
|------|----------------|
| **AttackEffect** | Common shape for effects that **target defenses** and may inflict conditions or harm |
| **Damage** | Inflicts hit point loss; typically vs Toughness or similar |
| **Affliction** | Imposes conditions; resistance path may be **fixed or configurable** |

**`Damage`** and **`Affliction`** **specialize** **`AttackEffect`** where shared structure (attack roll → resistance) applies.

### 2.5 Modifiers — cross-cutting

| Type | Responsibility |
|------|----------------|
| **Modifier** | Abstract adjustment (cost, scope, trade-off) |
| **Extra** | Optional add-on that increases effect or flexibility |
| **Flaw** | Limitation that reduces cost or scope |

Modifiers are categorized by **behavior**, not by book chapter.

---

## 3. OOD — collaborations (summary)

```text
Power ──contains/applies──► Effect ──may specialize──► AttackEffect ◄──specialize── Damage
                                                              ▲
                                                              └── Affliction

Trait ◄──used for bonuses── Check (SkillCheck, AbilityCheck, …)
Defense ◄──target of── AttackCheck
Stamina ◄──resistance path── ResistanceCheck / Affliction (where applicable)

Modifier ──attaches to──► Power | Effect (extras/flaws)
```

---

## 4. What commonly goes wrong (guardrails)

1. **TOC = types** — Chapter headings (e.g. “Sensory Effects”) describe **shelves**, not Java-style classes per paragraph.
2. **Promoting examples** — A worked example in a sidebar is **evidence**, not automatically a **concept** row.
3. **Collapsing Power and Effect** — Breaks container semantics and breaks critic alignment.
4. **Ignoring resistance variety** — Affliction vs Damage vs generic AttackCheck need distinct **resistance** narratives; model explicitly, don’t overload one “save” type.
