#!/usr/bin/env python
from sys import argv, exit
from program import run

if __name__ == '__main__':

	if len(argv) is not 2:
		print(f"[!] Usage: argv[0] <project name>")
		exit(0)
	else:
		run(argv[1])

