#!/usr/bin/env python
from os import strerror


if __name__ == '__main__':
	data = bytearray(10)

	for i in range(len(data)):
		data[i] = 10 + i

	try:
		bf = open('file.bin', 'wb')
		bf.write(data)
		bf.close()
	except IOError as e:
		print("IO error occurred: ", strerr(e.errno))

	try:
		bf = open('file.bin', 'rb')
		bf.readinto(data)
		bf.close()

		for b in data:
			print(hex(b), end='')

	except IOError as e:
		print("IO error occurred: ", strerr(e.errno))

	print()
