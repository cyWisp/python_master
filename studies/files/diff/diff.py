#!/usr/bin/env python
from sys import argv

if __name__ == '__main__':

	if len(argv) > 3: print("[x] Too many arguments!")
	elif len(argv) < 3: print("[x] Too few arguments!")
	else:
		if argv[1] == argv[2]: print("[+] Match!")
		else: print("[x] No match!")
