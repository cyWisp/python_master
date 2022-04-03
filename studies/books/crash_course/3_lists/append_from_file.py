#!/usr/bin/env python
import os

def main():

	names = []

	try:
		with open('names.txt', 'r') as input_file:
			for line in input_file:
				names.append(line)
	except IOError as io_error:
		print("[x] File IO Error: {}".format(io_error))
	finally:
		input_file.close()

	print("Names in list:\n")

	for index, name in enumerate(names):
		index = index + 1
		print('{}.{}'.format(str(index), name))

if __name__ == '__main__':
	main()
