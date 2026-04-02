"""
Emit a native diagrams.net (.drawio) class view from map-model-spec.json.

Implementation lives in **agile_bots** (`synchronizers.story_io.map_model_spec_drawio`) and uses the
same **mxfile / mxCell** pipeline as story-map Draw.io output — not Mermaid.

From skill root (with conf/abd-config.json → workspace containing map-model-spec.json):

    python scripts/render_map_model_class_diagram.py

Requires **agile_bots_root** in conf/abd-config.json or **AGILE_BOTS_ROOT** env.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

_SKILL_ROOT = Path(__file__).resolve().parents[1]
if str(_SKILL_ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(_SKILL_ROOT / "scripts"))

from _config import agile_bots_root, map_model_spec_path, output_dir  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser(
        description="map-model-spec.json → map-model-class-diagram.drawio (via agile_bots)"
    )
    ap.add_argument(
        "--output",
        "-o",
        type=Path,
        help="Write .drawio here (default: <output_dir>/map-model-class-diagram.drawio)",
    )
    args = ap.parse_args()

    spec = map_model_spec_path()
    if not spec.is_file():
        print(f"abd-maps-models-specs: map-model-spec not found: {spec}", file=sys.stderr)
        sys.exit(1)

    root = agile_bots_root()
    script = root / "scripts" / "render_map_model_drawio.py"
    if not script.is_file():
        print(f"abd-maps-models-specs: agile_bots script not found: {script}", file=sys.stderr)
        sys.exit(1)

    out = args.output if args.output else (output_dir() / "map-model-class-diagram.drawio")
    out = out.resolve()
    cmd = [sys.executable, str(script), "-i", str(spec), "-o", str(out)]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
