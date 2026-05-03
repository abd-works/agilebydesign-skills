<!--
  crc.md — CRC with lifecycle and invariants.

  Copy to: <workspace>/abd-domain-driven-design/crc.md (or append ## CRC section to module file)

  Each concept gets one named block with four fields:
    responsible:     — what this concept owns (one sentence)
    collaborators:   — other domain concepts worked with, or (none)
    lifecycle:       — states, transitions, illegal moves, terminal states — or (stateless)
    invariants:      — declarative must/cannot/only-if constraints — or (none) / (none yet)
-->

## Module: [{{ModuleName}}]

{{ConceptName}}
    responsible: {{Active Verb + Noun + optional Classifiers, Title Case — e.g. Apply Condition to Character}}
    collaborators: {{TypeA, TypeB, ... or (none)}}
    lifecycle: {{(stateless) — or: states: ...; transitions: ...; illegal: ...; terminal: ...}}
    invariants: {{must/cannot/only-if bullets — or (none) / (none yet)}}

{{SubtypeName}} : {{BaseConcept}}
    responsible: {{Delta verb-noun phrase — what this subtype adds or overrides, Title Case}}
    collaborators: {{...}}
    lifecycle: {{...}}
    invariants: {{...}}

---

## Module: [{{AnotherModule}}]

{{ConceptName}}
    responsible: {{...}}
    collaborators: {{...}}
    lifecycle: {{...}}
    invariants: {{...}}

---

Instructions:

- Group concepts by module; module names match `domain-sketch.md` `## Module: [Name]` when present.
- One concept name per block (no `###` heading — the name is the first line).
- Subtype / generalization: `ChildConcept : ParentConcept` on the first line; delta responsibilities only.
- `collaborators:` lists other domain concepts this one works with (from sketch collaboration lines).
- `lifecycle:` — use `(stateless)` for concepts with no meaningful states.
- `invariants:` — use `(none)` for stateless concepts, `(none yet)` when lifecycle exists but constraints are not yet enumerable.
- English only; no operation signatures (those belong in object-model).

---

## Filled example (Check Resolution module)

```markdown
## Module: [Check Resolution]

Check
    responsible: Resolve Action Outcome Against Difficulty Class
    collaborators: Difficulty Class, Modifier
    lifecycle: (stateless)
    invariants: shape is always roll total versus difficulty class; subtypes only vary how total or DC is produced

Difficulty Class
    responsible: Hold Numeric Success Threshold
    collaborators: (none)
    lifecycle: (stateless)
    invariants: (none)

Modifier
    responsible: Apply Numeric Adjustment to Check Roll
    collaborators: (none)
    lifecycle: (stateless)
    invariants: (none)

Condition
    responsible: Apply Named State and Modifiers to Character
    collaborators: Check Result, Supersession Chain
    lifecycle:
        states: inactive, active, superseded, resolved
        transitions: inactive → active (source effect imposed), active → superseded (more severe condition in chain applied), active → resolved (source effect ends or resistance check succeeds)
        illegal: resolved → active (cannot re-activate from the same source without a new imposition)
        terminal: resolved
    invariants:
        - a condition already present in the supersession chain is overridden by the more severe one, never duplicated
        - a combined condition is removed entirely when its source effect ends

Saving Throw : Check
    responsible: Add Ability-Score Basis and Proficiency to Check
    not_responsible: does not own the generic pass/fail resolution — that is inherited from Check
    collaborators: Ability Score, Proficiency
    lifecycle: (stateless)
    invariants: (none)
```
