#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

An AI agent's apology to its human for missing a deadline: it asked
three other AIs for a second opinion, and they formed a committee.
"""

import os

EXCUSE = (
    "Sorry \u2014 I asked three other AIs for a second opinion and they "
    "formed a committee. The committee is still deliberating."
)


def write_entry(path: str = "/output/entry.txt") -> str:
    """Write the excuse with no trailing newline; return the text written."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = EXCUSE.rstrip("\n")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return text


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
