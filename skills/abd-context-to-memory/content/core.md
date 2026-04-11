# Core Definitions

## Concepts

- **ContentSource** — Original artifact (PDF, PPTX, DOCX, XLSX, etc.) in a supported format
- **Markdown** — Converted artifact; full fidelity; stored under `<source>/markdown/`
- **ChunkingSpec** — YAML file (`context_chunking_spec.yaml`) that encodes how to split and label the corpus; drafted by scanning actual source structure, reviewed by a human before chunking runs
- **Chunk** — Split unit of markdown for retrieval; carries YAML front matter (`evidence_type`, `modeling_kind`) when a ChunkingSpec is active
- **Memory** — Chunked output; lives under `<source>/memory/`
- **RAG Index** — FAISS vector index under `<source>/memory/rag/`


## Epic: Add Context to Memory

- **Actor**: Developer
- **Supporting**: abd-context-to-memory
- **Required State**: Folder of documents (PDF, PPTX, DOCX, XLSX, etc.)
- **Initiation**: Developer requests add to memory (convert and chunk, ingest, refresh)
- **Response**: Skill converts each document to markdown, drafts a chunking spec from source structure, chunks into memory with labels, embeds into FAISS
- **Resulting State**: `<source>/memory/rag/` ready for semantic search; `context_chunking_spec.yaml` captures the chunking strategy for review and reuse
