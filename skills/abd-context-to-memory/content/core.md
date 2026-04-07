# Core Definitions

## Concepts

- **ContentSource** — Original artifact (PDF, PPTX, DOCX, XLSX, etc.) in a supported format
- **Markdown** — Converted artifact; full fidelity; stored under `<source>/markdown/`
- **Chunk** — Split unit of markdown for retrieval; one chunk per slide, heading section, or whole file
- **Memory** — Chunked output; lives under `<source>/memory/`
- **RAG Index** — FAISS vector index under `<source>/memory/rag/`

## Epic: Add Context to Memory

- **Actor**: Developer
- **Supporting**: abd-context-to-memory
- **Required State**: Folder of documents (PDF, PPTX, DOCX, XLSX, etc.)
- **Initiation**: Developer requests add to memory (convert and chunk, ingest, refresh)
- **Response**: Skill converts each document to markdown, chunks into memory, embeds into FAISS
- **Resulting State**: `<source>/memory/rag/` ready for semantic search
