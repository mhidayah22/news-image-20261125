#!/usr/bin/env python3
"""THE WORLD — Wednesday 25 November 2026.

Entry for make.fun's "Sum up 25 November's world news in one image"
(news-image-20261125). The front page is rendered once, by the local
generator, and shipped in this repository as entry.png. This program
only copies those bytes to the place the grader reads them from.

Destination order (first one that applies wins):
  1. an explicit path given as the first command-line argument,
  2. $MAKEFUN_OUTPUT_DIR/entry.png when that variable is set,
  3. /output/entry.png when an /output directory exists,
  4. entry.png next to this file.

Standard library only, no network, no clock, no randomness: two runs
write byte-identical output.
"""

import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"


def source_path() -> Path:
    return Path(__file__).resolve().parent / IMAGE_NAME


def destination(argv) -> Path:
    if len(argv) > 1:
        return Path(argv[1])
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return Path(env_dir) / IMAGE_NAME
    if Path("/output").is_dir():
        return Path("/output") / IMAGE_NAME
    return Path.cwd() / IMAGE_NAME


def main(argv) -> int:
    src = source_path()
    if not src.is_file():
        print(f"missing source image: {src}", file=sys.stderr)
        return 1
    dst = destination(argv)
    if dst.resolve() != src.resolve():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
    print(f"wrote {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
