#!/usr/bin/env python
from sys import argv


if __name__ == '__main__':
	try:
		int(argv[1])
	except BaseException as e: print(f"{e.__class__.__name__}: {e}")
	else: print("its fine")

	try:
		assert int(argv[1]) > 1 and int(argv[1]) < 5
	except AssertionError: print("nope")
	else: print("its fine")
