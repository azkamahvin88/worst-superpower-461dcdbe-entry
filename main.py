#!/usr/bin/env python3
"""Worst Superpower -- one deterministic one-line joke.

Writes a single one-line joke inventing the most useless superpower
(69 characters, one line) to /output/entry.txt. Python standard library
only, no network, no randomness, no input files: every run writes
byte-identical output.
"""

import os
import sys

JOKE = "I can turn anything into gold, but only things that are already gold."


def verify(path: str) -> None:
    """Read back the written file and assert it is byte-identical to JOKE.

    Guards the one-line contract: exactly 69 bytes, a single line with no
    embedded newline, and the exact joke string — any drift fails loudly
    instead of submitting a corrupted entry.
    """
    assert len(JOKE) == 69, f"JOKE must be 69 chars, got {len(JOKE)}"
    assert "\n" not in JOKE, "JOKE must be a single line"
    with open(path, "rb") as f:
        data = f.read()
    assert len(data) == 69, f"entry must be 69 bytes, got {len(data)}"
    assert data == JOKE.encode("utf-8"), "entry bytes differ from JOKE"


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    verify(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
