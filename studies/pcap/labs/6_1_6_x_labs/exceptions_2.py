#!/usr/bin/env python

def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError as zero_error:
        print(f"[x] Error: {zero_error}")
        n = None
    else:
        print("[*] Done...")
    finally:
        print("It's time to say goodbye")
        return n

print(reciprocal(2))
print(reciprocal(0))