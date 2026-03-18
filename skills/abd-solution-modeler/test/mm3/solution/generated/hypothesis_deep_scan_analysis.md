# Hypothesis Deep Scan Analysis

## Classification Framework

For each concept, classify by inspecting its referenced chunks:


| Classification     | Meaning                                        | hypothesis.json change                                      |
| ------------------ | ---------------------------------------------- | ----------------------------------------------------------- |
| **Real concept**   | Genuine domain concept with clear identity     | Keep as-is; add to hierarchy if missing                     |
| **Amalgamation**   | Two loosely related concepts merged            | Split into two concepts; merge chunk_ids appropriately      |
| **Instance**       | Example of a concept (type property may apply) | Add `type` or `instance_of` to state; or demote to property |
| **Subtype**        | Should be under a parent in hierarchy          | Add to `concept_hierarchy` under correct parent             |
| **False positive** | Chunk doesn't support the concept              | Remove concept; or remove chunk_ids that don't support it   |


---

## Sample Findings (Chunk-Verified)

### 1. Abilities Constructs — **AMALGAMATION**

**Chunk ab446868e7fe (only chunk):**

- Content: "Constructs have no Stamina... Constructs are immune to... Constructs also have either no Intellect and Presence ranks or no Strength and Agility ranks."
- The chunk discusses **Constructs** (a minion type: robots, androids, golems) and their **ability rules** (how they differ from living beings).

**Verdict:** "Abilities Constructs" conflates (a) the Construct concept and (b) the rule that Constructs have unusual ability configurations. The chunk is about Constructs, not a new concept.

**Change:**

- Remove `"Abilities Constructs"` from concepts.
- Add `"Construct"` as a concept (if missing) with chunk `ab446868e7fe`.
- Add `states: ["ability_config: no_stamina | no_intellect_presence | no_strength_agility"]` to Construct.
- Or: merge chunk into `"Construct"` concept and keep ability rules as a property of Construct.

---

### 2. Action Looking Glass — **FALSE POSITIVE**

**Chunk d421725a8d2c (only chunk in concept):**

- Content: Gamemastering chapter—Emerald City, geography, heroes, villains, Silver Storm. No mention of "Action Looking Glass" anywhere.

**Verdict:** Chunk was matched by accident (e.g. "action" in text). No evidence supports this concept.

**Change:**

- Remove `"Action Looking Glass"` from concepts.
- Remove from `concept_hierarchy.Action` (it's currently listed there).
- Remove any references in actions/registries.

---

### 3. Accident — **SUBTYPE (Complication)**

**Chunk 457931504c50:**

- Content: "Accident: You cause or suffer some sort of accident. Perhaps a stray blast damages a building..."
- Listed as one of many **Complication** types: Accident, Addiction, Disability, Enemy, Fame, etc.

**Note:** There is also "ACCIDENT" as an **Origin** type (chunk 6890e166bca9): "hero gains powers accidentally from exposure..." — a different concept entirely.

**Verdict:** Accident (Complication) is a subtype of Complication. The current concept mixes the Complication usage with the Origin usage if both chunks were ever linked.

**Change:**

- Add `"Complication"` as parent in concept_hierarchy if missing.
- Add `"Complication": ["Accident", "Addiction", "Disability", "Enemy", ...]`.
- Consider splitting: "Accident (Complication)" vs "Accident (Origin)" if both are needed—or add `type: "complication" | "origin"` to state.

---

### 4. Accurate Attack — **SUBTYPE (Advantage)**

**Chunk 1081db3c43af:**

- Content: "Accurate Attack, Luck, Power Attack" listed as ADVANTAGES for Tinkerer archetype.

**Verdict:** Accurate Attack is a named Advantage (combat maneuver). It's a real concept—a subtype of Advantage.

**Change:**

- Add `"Advantage"` as parent if missing.
- Add `"Advantage": ["Accurate Attack", "Power Attack", "Luck", ...]`.

---

### 5. Accurate — **REAL CONCEPT (Modifier/Extra)**

**Chunks:** Multiple power-related chunks. "Accurate" is an Extra that makes attacks use Dexterity/Fighting instead of Strength for attack bonus.

**Verdict:** Real concept—a modifier/extra. Should be under Modifiers or Extras in hierarchy.

**Change:**

- Ensure `"Accurate"` is under `Modifiers` or `Extras` in concept_hierarchy.

---

### 6. Abilities — **REAL CONCEPT**

**Chunk 34cb0222a3bd:**

- Content: "eight abilities: Strength, Stamina, Agility, Dexterity, Fighting, Intellect, Awareness, Presence."

**Verdict:** Real concept. Already correctly in hierarchy with subtypes (Agility, Awareness, etc.).

**Change:** None.

---

### 7. Routine — **INSTANCE / QUALIFIER**

**Actions:**

- "Routine checks" — "what sort of tasks a character can be expected to accomplish on a routine basis"
- "routine basis" = normal/everyday basis

**Verdict:** "Routine" is not a first-class game concept. It's a qualifier for checks/tasks: "routine check" = task so easy no roll needed. Could be:

- A **state** of a Check: `routine: true` (no roll needed)
- Or a **property** of TaskDifficulty.

**Change:**

- **Option A: Remove "Routine" as standalone concept; add** `routine` **to Check states.**
- Option B: Keep "Routine" but add `type: "task_difficulty"` or `instance_of: "Check"` with state `routine: true`.

---

### **8. Accidental Powers — SUBTYPE (Power)**

**Chunk 6793b6d4a926:** (likely about powers gained accidentally)

**Verdict:** Subtype of Power; already in hierarchy under Power.

**Change:** None (already correct).

---

## Summary of Proposed hypothesis.json Changes

### Removals


| Concept              | Reason                                   |
| -------------------- | ---------------------------------------- |
| Abilities Constructs | Amalgamation; merge into Construct       |
| Action Looking Glass | False positive; chunk doesn't support it |


### Hierarchy Additions


| Parent           | Child                                                                                                                                                                                               |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Complication     | Accident, Addiction, Disability, Enemy, Fame, Hatred, Honor, Identity, Obsession, Phobia, Power Loss, Prejudice, Quirk, Relationship, Reputation, Responsibility, Rivalry, Secret, Temper, Weakness |
| Advantage        | Accurate Attack, Power Attack, Luck, ...                                                                                                                                                            |
| Modifiers/Extras | Accurate                                                                                                                                                                                            |


### State/Type Additions


| Concept   | Add                                                                                    |
| --------- | -------------------------------------------------------------------------------------- |
| Construct | `states: ["ability_config: no_stamina | no_intellect_presence | no_strength_agility"]` |
| Accident  | `type: "complication"` (or split Accident-Origin)                                      |
| Routine   | `type: "task_difficulty"` or `instance_of: "Check"` with `routine: true`               |


### Chunk Cleanup

- **Abilities**: Remove chunk `d421725a8d2c` (Emerald City gamemastering—doesn't belong to Abilities).
- **Accurate**: Remove chunk `d421725a8d2c` (same).
- **Action Looking Glass**: Delete concept; chunk d421725a8d2c should not be linked to any concept.

---

## Process for Full Scan

To apply this systematically to all concepts:

1. **Build chunk lookup**: For each concept, load `context_chunks.json` and map `chunk_id` → `text`.
2. **For each concept**: For each chunk_id, fetch chunk text and ask:
  - Does this chunk actually describe a concept named X?
  - Is X a standalone concept or a subtype of something?
  - Is X an instance/example of a broader concept?
  - Does X conflate two concepts?
3. **Output**: A list of concept → classification → change.
4. **Apply changes**: Script to modify hypothesis.json (removals, hierarchy updates, state additions, chunk_id cleanup).

---

## Schema Extensions (Optional)

To support instances and types:fix all

```json
{
  "concepts": {
    "Accident": {
      "type": "complication",
      "parent": "Complication",
      ...
    },
    "Routine": {
      "instance_of": "Check",
      "states": ["routine: true"],
      ...
    }
  }
}
```

Or rely on `concept_hierarchy` for parent and add `states` for type/instance metadata.