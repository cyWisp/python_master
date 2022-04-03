#!/usr/bin/env python

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError as zero_error:
        print(f"[x] Error: {zero_error}")
        return None
    else:
        print("[*] Done...")
        return n

print(reciprocal(2))
print(reciprocal(0))
