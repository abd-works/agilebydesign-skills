"""Test cursor-agent: run it, stream output, detect CHECKPOINT, prompt user, resume."""
import os, subprocess, sys, tempfile
from pathlib import Path

WORKSPACE = r"C:\dev\abd-pet-store-demo"
BINARY = r"C:\Users\thoma\AppData\Local\cursor-agent\cursor-agent.cmd"

# ---------------------------------------------------------------------------
# Load API key
# ---------------------------------------------------------------------------
secrets = Path(__file__).parent / "conf" / ".secrets"
api_key = None
for line in secrets.read_text().splitlines():
    if line.startswith("CURSOR_API_KEY="):
        api_key = line.split("=", 1)[1].strip().strip('"').strip("'")
        break

if not api_key:
    print("ERROR: no CURSOR_API_KEY in conf/.secrets")
    sys.exit(1)

print(f"API key: {api_key[:12]}...")


def run_agent(prompt: str, label: str = "agent") -> int:
    """Run cursor-agent with prompt, stream output line by line. Returns exit code."""
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8")
    tmp.write(prompt)
    tmp.close()

    cmd = [
        BINARY,
        "-p", "--trust", "--force",
        "--output-format", "text",
        "--workspace", WORKSPACE,
        f"Read and follow every instruction in {tmp.name}",
    ]

    env = dict(os.environ)
    env["CURSOR_API_KEY"] = api_key

    print(f"\n[{label}] Starting...")
    print("-" * 60)
    sys.stdout.flush()

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
    )

    for line in proc.stdout:
        print(line, end="", flush=True)

    proc.wait()
    print()
    print("-" * 60)
    print(f"[{label}] Exit: {proc.returncode}")
    sys.stdout.flush()
    return proc.returncode


# ---------------------------------------------------------------------------
# Turn 1: agent asks user a question and signals CHECKPOINT
# ---------------------------------------------------------------------------
TURN1_PROMPT = """\
You are a delivery agent running in headless mode.

1. Print exactly this line (no extra text before it):
   What is your favourite colour?
2. Then print exactly this line:
   CHECKPOINT: awaiting operator input. Reply with your answer.
3. Then stop. Do not print anything else.
"""

run_agent(TURN1_PROMPT, label="turn-1")

# ---------------------------------------------------------------------------
# Harness detects CHECKPOINT and prompts user
# ---------------------------------------------------------------------------
print()
print("=" * 60)
print("CHECKPOINT detected — harness prompting operator")
print("=" * 60)
try:
    answer = input("Your answer: ").strip()
except EOFError:
    print("\nERROR: no interactive terminal — run this script in a real PowerShell window:")
    print("  cd c:\\dev\\agilebydesign-skills && python -u test_cursor_agent.py")
    sys.exit(1)
if not answer:
    answer = "blue"
print(f"Recorded: {answer!r}")

# ---------------------------------------------------------------------------
# Turn 2: resume with user's answer
# ---------------------------------------------------------------------------
TURN2_PROMPT = f"""\
You are a delivery agent resuming after a CHECKPOINT.

The operator answered: {answer!r}

Print exactly this: RESUMED — operator said: {answer}
Then stop.
"""

run_agent(TURN2_PROMPT, label="turn-2")
print("\nTest complete.")
