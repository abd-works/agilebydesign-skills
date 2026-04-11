# RAG Semantic Retrieval

When the user asks about content in memory, run semantic search and inject results.

## Trigger Phrases

Run `search_memory "<query>"` when the user says:

- "use memory", "search memory", "what does memory say"
- "from our content", "from ABD materials", "from our decks"
- "what do we have on [topic]"
- Asks about Agile, training, proposals, service offerings, or any ingested materials

## Agent Flow

1. **Derive query** — Extract a semantic query from the user's question.
2. **Run search** — From the workspace root:
   ```bash
   python skills/abd-context-to-memory/scripts/search_memory.py "<query>" --rag <source>/memory/rag --k 5
   ```
3. **Inject results** — Use the returned chunks in your response.
4. **Cite sources** — Include path and slide/section when using retrieved content. If chunks have front matter, also note `evidence_type` / `modeling_kind` to signal how much weight to give the result.

## Requirements

- RAG deps: `pip install -r skills/abd-context-to-memory/requirements-rag.txt`
- `OPENAI_API_KEY` set
- Index exists: run `index_memory.py --path <source>` first

## Output Layout

```
<source>/memory/rag/
  index.faiss
  metadata.json
```

## Chunk front matter (when spec was active during chunking)

Results may include chunks with YAML front matter. Use the labels to calibrate your response:

| `modeling_kind` | How to use |
|----------------|-----------|
| `rule` / `definition` | Cite as authoritative — normative content |
| `example` | Use as illustration only, not as ground truth |
| `noise` / `structural_only` | Low weight — boilerplate or navigation chrome |
