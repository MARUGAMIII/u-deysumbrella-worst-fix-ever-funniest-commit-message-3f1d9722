#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message for a bug fix that made everything worse
to /output/entry.txt, exactly as the competition gate requires:
UTF-8 text, 1 to 100 characters, a single line, no trailing newline.

The fix: the crash is gone, because every last user is gone too.
The entry is validated against the gate before anything is written,
so a bad entry fails loudly here instead of at judging time.
"""

import os

ENTRY = "fix: stopped the crash by deleting all users"


def main() -> None:
    # Gate check: the entry must stay exactly one line, 1-100 chars.
    if not (1 <= len(ENTRY) <= 100) or "\n" in ENTRY:
        raise SystemExit(f"entry violates gate: {ENTRY!r}")
    if ENTRY != ENTRY.strip():
        raise SystemExit(f"entry has leading/trailing whitespace: {ENTRY!r}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
