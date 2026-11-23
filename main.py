#!/usr/bin/env python3
"""news-image-20261123 entrypoint.

Copies the pre-rendered front page (entry.png) to /output/entry.png.
Standard library only; deterministic: the same bytes every run.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs("/output", exist_ok=True)
    size = os.path.getsize(SRC)
    if size > 1048576:
        raise SystemExit("entry.png is %d bytes, over the 1 MiB limit" % size)
    shutil.copyfile(SRC, DST)
    digest = hashlib.sha256(open(DST, "rb").read()).hexdigest()
    print("wrote %s (%d bytes) sha256=%s" % (DST, size, digest))


if __name__ == "__main__":
    main()
