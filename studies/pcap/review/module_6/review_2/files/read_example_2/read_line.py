#!/usr/bin/env python
from os import strerror

if __name__ == '__main__':
	try:
		with open("./text.txt", "r+") as test:
			lines = [x.strip() for x in test]
	except IOError as e:
		print("[x] Error: ", strerr(e.errno))
	finally: test.close()

	line_count = char_count = 0

	for l in lines:
		line_count += 1
		for c in l:
			char_count += 1

	for l in lines:
		print(l)

	print("Lines: ", line_count)
	print("Characters: ", char_count)


