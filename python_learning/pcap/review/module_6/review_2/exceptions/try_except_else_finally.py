#!/usr/bin/env python
from sys import argv

def reciprocal(n):
	try:
		n = 1 / n
	except:
		print("[x] Division by zero!")
		n = None
	else:
		print("[+] Division succeeded!")
	finally:
		print(f"[+] Execution completed...")
		return n

if __name__ == '__main__':
	print(reciprocal(int(argv[1])))
