"""
Full pipeline: convert → draft spec → chunk → embed into local FAISS vector store.

**Ownership:** Step 1 (**convert** + ``pdf_markdown_post``) rewrites extracted markdown so structure
is findable. Step 2 (**spec**) only observes and drafts YAML. Step 3 (**chunk**) splits along
existing boundaries—it does not compose manuscript structure (see skill *Chunker vs converter*).

Usage:
  python index_memory.py [--path <source_folder>]                        # full pipeline (--path defaults from _config)
  python index_memory.py --path <source_folder> --skip-convert           # skip convert
  python index_memory.py --path <source_folder> --skip-spec              # skip spec draft
  python index_memory.py --path <source_folder> --skip-convert --skip-spec  # chunk + embed only
  python index_memory.py --rebuild [--path <source_folder>]               # rebuild index from existing chunks

Steps:
  1. Convert  — source docs → markdown/ (post-process PDFs for headings/banners here)
  2. Spec     — structural reports → markdown/; drafted YAML → memory/context_chunking_spec.yaml (skipped if present)
  3. Chunk    — apply spec → memory/ (split only; no source .md rewrite)
  4. Embed    — chunks → memory/rag/ (FAISS)

Run from your topic/corpus folder or set CONTENT_MEMORY_ROOT.
"""

import subprocess
import sys
from pathlib import Path

from _config import ROOT

SCRIPTS = Path(__file__).resolve().parent
SPEC_FILENAME = "context_chunking_spec.yaml"


def run(script: str, args: list[str], cwd: Path) -> None:
    result = subprocess.run([sys.executable, str(SCRIPTS / script)] + args, cwd=str(cwd))
    if result.returncode != 0:
        print(f"ERROR: {script} failed.")
        sys.exit(1)


def main():
    args = sys.argv[1:]

    skip_convert = "--skip-convert" in args
    skip_spec = "--skip-spec" in args
    rebuild = "--rebuild" in args
    args = [a for a in args if a not in ("--skip-convert", "--skip-spec", "--rebuild")]

    path_idx = next((i for i, a in enumerate(args) if a == "--path"), None)
    if path_idx is not None and path_idx + 1 < len(args):
        src = Path(args[path_idx + 1]).resolve()
    else:
        src = ROOT.resolve()
        print(f"Using default topic folder (CONTENT_MEMORY_ROOT or cwd): {src}")
    if not src.exists():
        print(f"ERROR: source folder not found: {src}")
        sys.exit(1)

    memory_dir = src / "memory"
    memory_dir.mkdir(parents=True, exist_ok=True)

    total_steps = 4
    step = 0

    # Step 1: Convert
    step += 1
    if not skip_convert:
        print(f"[{step}/{total_steps}] Converting documents in {src} → markdown/")
        run("convert_to_markdown.py", ["--memory", str(src)], cwd=src)
    else:
        print(f"[{step}/{total_steps}] Skipping convert (--skip-convert)")

    # Step 2: Structural reports → markdown/; chunking spec → memory/ (skipped if already there, unless --force on draft)
    step += 1
    spec_path = memory_dir / SPEC_FILENAME
    if skip_spec:
        print(f"[{step}/{total_steps}] Skipping spec draft (--skip-spec)")
    else:
        print(
            f"[{step}/{total_steps}] Structural scan → markdown/; chunking spec → {spec_path.name} under memory/ when new"
        )
        run("draft_chunking_spec.py", ["--path", str(src)], cwd=src)
        print()
        print("  ─────────────────────────────────────────────────────")
        print(f"  Review: markdown/structural_scan_report.*  |  Spec: {spec_path} (if drafted)")
        print("  RECOMMENDED: Review context_chunking_spec.yaml before continuing.")
        print("  Edit boundaries, taxonomy, and defaults to match your sources.")
        print("  Then re-run with --skip-spec (or just continue — the spec will be used as-is).")
        print("  ─────────────────────────────────────────────────────")
        print()

    # Step 3: Chunk
    step += 1
    print(f"[{step}/{total_steps}] Chunking markdown → {memory_dir}")
    run("chunk_markdown.py", ["--path", str(src), "--output", str(memory_dir)], cwd=src)

    # Step 4: Embed
    step += 1
    print(f"[{step}/{total_steps}] Embedding chunks → {memory_dir / 'rag'}")
    embed_args = ["--path", str(memory_dir)]
    if rebuild:
        embed_args.append("--replace")
    run("embed_and_index.py", embed_args, cwd=src)

    print(f"\nDone. Index: {memory_dir / 'rag'}")


if __name__ == "__main__":
    main()
