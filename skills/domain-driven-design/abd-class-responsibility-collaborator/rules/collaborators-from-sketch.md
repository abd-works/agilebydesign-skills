# Rule: Collaborators trace to sketch collaborations and subtype edges

**Scanner:** Manual review

The collaborator column in each CRC block must list domain concepts that appear in the domain sketch's behavior bullets or subtype edges for that concept. No collaborator may be invented. An empty collaborator column must contain a value description in parentheses (for primitives/enums) or be explicitly empty only when the responsibility truly has no collaborating concept.

## DO

- List collaborators that correspond to concepts named in the behavior bullet.

  **Example (pass):** Sketch says "supersedes a less severe condition from the same source"; CRC has `supersede | Condition`.

- Use a parenthetical value description for primitive/enum collaborators.

  **Example (pass):** `active status | (active or inactive)`

## DO NOT

- Invent collaborators that have no basis in the domain sketch.

  **Example (fail):** CRC block lists `Logger, EventBus` but neither concept appears anywhere in the sketch.

- Leave the collaborator column blank without explanation.

  **Example (fail):** `supersede |` with nothing on the right.

**Source:** Engagement convention (class-responsibility-collaborator skill).
