#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters.

Writes a single Wi-Fi network name to /output/entry.txt.

The name is the whole entry: a petty domestic standoff told in one
line. Someone in the house has cut the Wi-Fi off, and the network
name itself is the ultimatum -- Dave gets his internet back when he
apologizes. The passer-by reading the network list instantly knows
there is a Dave, that Dave did something, and that someone else in
the house is furious enough to hold the router hostage over it.
"""

import os

ENTRY = "No WiFi Till You Apologize, Dave"

MAX_CHARS = 32


def main() -> None:
    # The sealed gate only accepts 1-32 characters, so never emit a
    # name that would fail it: fail loudly here instead of writing
    # an invalid entry.
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(ENTRY)} characters, must be 1-{MAX_CHARS}"
        )
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    # Write exactly the name: no trailing newline, so the file stays
    # within the 32-character gate (the name is exactly 32 chars).
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
