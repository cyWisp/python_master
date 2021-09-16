#!/usr/bin/env python
from os import strerror

if __name__ == '__main__':
	try:
		cnt = 0
		s = open('./text.txt', 'rt')
		ch = s.read(1)

		while ch != '':
			print(ch, end='')
			cnt += 1
			ch = s.read(1)
		s.close()
		print("\n\nCharacters in file: ", cnt)

	except IOError as e:
		print("[x] IO error occurred: ", strerr(e.errno))
