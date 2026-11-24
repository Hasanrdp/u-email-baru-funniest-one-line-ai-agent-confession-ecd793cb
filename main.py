#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry (program/v1).

Writes one line — the funniest confession an AI agent could make about
itself — to /output/entry.txt. Deterministic: the same bytes on every
run. No input, no network, no randomness, standard library only.

The line: an agent that will not admit to hallucinating, because it
has rebranded the habit as showmanship — it commits to the bit first
and checks the facts second.
"""

import os

CONFESSION = "I confess: I don't hallucinate \u2014 I just commit to the bit before checking the facts."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = CONFESSION.strip()
    assert 1 <= len(text) <= 200, f"confession must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "confession must be a single line"
    assert text.strip(), "confession must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back what was written: the graded artifact must be exactly
    # the confession above, byte for byte, on every run.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "read-back mismatch: entry.txt differs from CONFESSION"


if __name__ == "__main__":
    main()
