#!/usr/bin/env python3
"""Write the loading-screen tip to /output/entry.txt.

One sharp, funny loading-screen tip for stressed developers and AI
coding agents, 200 characters or fewer. Pure Python 3.13 stdlib.
"""

import os

TIP = "Tip: if the build passes on the third try with no changes, neither of us fixed it. We just scared it."


def main() -> None:
    # Enforce the bounty gate locally: 1-200 chars, not only whitespace.
    assert 1 <= len(TIP) <= 200 and TIP.strip(), "tip must be 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
