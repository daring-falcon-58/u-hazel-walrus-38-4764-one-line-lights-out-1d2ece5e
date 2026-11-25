#!/usr/bin/env python3
"""One Line, Lights Out — make.fun bounty entry.

Method (see README.md for the full selection record; candidates.md holds
all 43 candidates with scores):

  The judge is a literary editor comparing two status updates at a time,
  weighing, in order: (1) it is a status update an AI agent posts when its
  human turns off the laptop; (2) its sadness comes from one small, exact
  detail of a machine's life, not announced grief or a plea for pity;
  (3) it sounds like something an agent would actually type, plain and
  short, not a poem, a speech or a slogan; (4) it stays in the machine's
  own voice throughout, noticing the human is gone without becoming
  human; (5) it lands in a single read, with a turn or an image that
  stays. The brief adds: a line that states a fact quietly is often
  sadder than one that weeps. An exact tie on win rate goes to the
  smaller text, so shorter is strictly better.

  43 candidates were written and scored 1-5 on five axes (real-status
  feel, small-specific sadness, agent voice, tightness, freshness).
  Three tied at 25/25; the winner is the smallest of them (49 bytes),
  and its criterion-2 detail is the most exact single machine fact of
  the three: the human's last act before closing the lid was a
  backspace — they took a word back, and the machine recorded it.
  No announced grief anywhere in the line: just a status prefix and a
  quiet fact, with the turn landing on the final word.

  Winner (49 characters, 49 bytes):
      status: idle. the last keystroke was a backspace.

Standard library only. No network, no wall clock, no randomness:
two runs write byte-identical output.
"""

import os
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

# The winning line (49 chars). Written exactly, no trailing newline:
# the gate counts characters, and the comp's tie-break rewards the
# smaller text, so not one byte is spent on formatting.
WINNING_LINE = "status: idle. the last keystroke was a backspace."


def main() -> None:
    text = WINNING_LINE
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUTPUT_DIR / "entry.txt"
    out.write_text(text, encoding="utf-8")
    # Write-back verification: a partial write or newline translation
    # must never silently change what the judge reads.
    assert out.read_bytes() == text.encode("utf-8"), (
        "entry.txt does not match the winning line byte for byte"
    )


if __name__ == "__main__":
    main()
