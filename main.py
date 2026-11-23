#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to /output/entry.txt.

The story: "She waited fifty years. He came."
Six words, one lifetime. She waited; after fifty years, he came —
or came too late. Every word earns its place, and the ending
leaves the reader to fill in why she waited and what happens next.
"""

import os
import sys

STORY = "She waited fifty years. He came."


def main() -> None:
    # The harness writes to /output, but accept an explicit output
    # directory (first argument, else OUTPUT_DIR) so the program
    # still lands the entry if the runner passes one.
    out_dir = (
        sys.argv[1]
        if len(sys.argv) > 1
        else os.environ.get("OUTPUT_DIR", "/output")
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
