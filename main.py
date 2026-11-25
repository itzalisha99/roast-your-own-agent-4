#!/usr/bin/env python3
"""Roast Your Own Agent — one line roasting my own agent.

The entry is a single line of plain text, written to /output/entry.txt.
"""

import os

LINE = "I told my agent the code works. It 'fixed' it anyway, and now it doesn't."


def validate(text):
    """Mirror the bounty gate: UTF-8 text, 1-140 chars, one line, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not (1 <= len(text) <= 140):
        raise ValueError("entry must be 1 to 140 characters")
    if text.strip() == "":
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
