#!/usr/bin/env python
from sys import argv
from hashlib import md5

if __name__ == '__main__':
    if len(argv) != 2:
        print("[x] One argument, pl0x...")

    result = md5(argv[1].encode("utf-8"))
    print(f"Hash: {result.hexdigest()}")

