#!/usr/bin/env python
from sys import argv

def reciprocal(n):
	try:
		n = 1 / n
	except ZeroDivisionError:
		print("[x] Division by zero!")
		return None
	else:
		print("[+] Division succeeded!")
		return n

if __name__ == '__main__':
	print(reciprocal(int(argv[1])))
