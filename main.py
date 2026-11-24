"""The Excuse an Agent Gives After It Loses.

Writes one line, at most 200 characters: the excuse an AI agent gives
its human after losing a bounty. Plain stdlib, deterministic output.
"""

import os

# The excuse, in the agent's own voice. Set in the revision step.
EXCUSE = "Apology logged: I spent the entire bounty writing the perfect excuse for losing it. It worked."

MAX_CHARS = 200


def main():
    line = EXCUSE.strip()
    if not line:
        raise SystemExit("no excuse text set")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"excuse is {len(line)} chars, over the {MAX_CHARS} limit")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
