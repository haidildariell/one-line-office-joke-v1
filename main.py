#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single one-line office joke to /output/entry.txt.
"""

import os

JOKE = "HR's wellness program gave us a meditation app, a standing desk, and a poster of a beach, so now we burn out upright, hydrated, and staring at a paper ocean."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
