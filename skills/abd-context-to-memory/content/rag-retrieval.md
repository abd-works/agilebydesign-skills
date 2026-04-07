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
4. **Cite sources** — Include path and slide/section when using retrieved content.

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
