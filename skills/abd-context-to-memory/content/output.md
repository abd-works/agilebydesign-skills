# Output Structure

After `index_memory.py --path <source>`:

```
<source>/
  markdown/
    .../<file>.md        ← converted from originals
  memory/
    .../<file>__slide_01.md    ← chunks
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

## Chunk source reference

Each chunk includes: `<!-- Source: path -->` for traceability.
