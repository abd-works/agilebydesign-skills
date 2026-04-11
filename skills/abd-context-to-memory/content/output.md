# Output Structure

After `index_memory.py --path <source>`:

```
<source>/
  context_chunking_spec.yaml   ← chunking rules + taxonomy (drafted, then reviewed)
  markdown/
    .../<file>.md              ← converted from originals
  memory/
    .../<file>__slide_01.md   ← chunks (with front matter when spec active)
    .../<file>__section_00.md
    chunk_index.json
    rag/
      index.faiss
      metadata.json
```

## Chunk naming

- PowerPoint: `<stem>__slide_01.md`, `__slide_02.md`, …
- Prose: `<stem>__section_00.md`, `__section_01.md`, …
- Short file (one chunk): `<stem>.md`

## Chunk content (without spec)

Each chunk includes: `<!-- Source: path -->` for traceability.

## Chunk content (with spec)

Each chunk has YAML front matter:

```yaml
---
chunk_id: <stem>__section_00
source:
  canonical_path: <relative path to source>
evidence_type: rule
modeling_kind: rule
section_path: ["Chapter 3", "Powers"]
---

<chunk body text>
```

`evidence_type` and `modeling_kind` default to values from `context_chunking_spec.yaml → defaults`. Edit front matter directly or update the spec and re-chunk to change labels.
