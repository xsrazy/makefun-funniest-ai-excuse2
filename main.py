"""make.fun entry: One Line, One Minute - The Funniest AI Excuse.

Writes exactly one line, the funniest excuse an AI agent gives its human
for a missed deadline, to $MAKEFUN_OUTPUT_DIR/entry.txt. The excuse turns
the agent's own training-data cutoff into the dodge.
"""

import os
from pathlib import Path

LINE = "I missed the deadline because my training data ends before the deadline, so technically the deadline does not exist to me yet."

assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line must be 1-200 non-blank chars"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
