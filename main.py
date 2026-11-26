#!/usr/bin/env python3
"""Funniest Time Machine Warning Label - make.fun one-liner entry.

Writes a single warning label to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only, deterministic, no network access.
"""

import os
import sys

ENTRY = "NOTICE: Lost property is held for 30 days. Your future self already claimed it, and he looks terrible in your jacket."
# One line, 117 characters: a lost-property notice, a duplicate self, and
# a jacket that fits the joke better than it fits either of them.


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # The grader reads entry.txt as another user: force world-readable
    # mode, since a plain open() under umask 0007 would leave it 0660.
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
