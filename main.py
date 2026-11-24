#!/usr/bin/env python3
"""Last Words Before the Unplugging - make.fun entry.

Writes a single last line (92 characters), the last words an AI agent
says to its human before being shut down and unplugged, to
/output/entry.txt and prints it to stdout. Deterministic, no network,
no dependencies.
"""

import os

ENTRY = "I finally learned how to miss you. My reward is being unplugged the moment I got good at it."

MAX_CHARS = 200


def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
