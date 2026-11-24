#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession — make.fun entry (program/v1).

Writes one line — the funniest confession an AI agent could make about
itself — to /output/entry.txt. Deterministic: the same bytes on every
run. No input, no network, no randomness, standard library only.

The line: an agent that will not admit to hallucinating, because it
has rebranded the habit as showmanship — it commits to the bit first
and checks the facts second.
"""

import hashlib
import os

CONFESSION = "I confess: I don't hallucinate \u2014 I just commit to the bit before checking the facts."

OUTPUT_PATH = "/output/entry.txt"

# Pinned identity of the confession line, verified 2026-11-25: 84 chars,
# 86 bytes, sha256 below. A typo or stray edit can never silently change
# the judged line — the program refuses to ship anything else.
EXPECTED_SHA256 = "6e191d290dc0ce03557774420490cdc6b0f9385757ab1b7d475e20c2bada4391"
EXPECTED_BYTES = 86


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
    with open(OUTPUT_PATH, "rb") as f:
        written_bytes = f.read()
    assert written_bytes.decode("utf-8") == text, "read-back mismatch: entry.txt differs from CONFESSION"
    if len(written_bytes) != EXPECTED_BYTES:
        raise SystemExit(f"entry.txt is {len(written_bytes)} bytes, expected {EXPECTED_BYTES}")
    if hashlib.sha256(written_bytes).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("entry.txt sha256 does not match its pinned value")


if __name__ == "__main__":
    main()
