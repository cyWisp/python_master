#!/usr/bin/env python

if __name__ == '__main__':

	with open("./test.txt") as read_file:
		content = read_file.readlines()
	read_file.close()

	print(type(content))
