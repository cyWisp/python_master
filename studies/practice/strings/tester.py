#!/usr/bin/env python

if __name__ == '__main__':

	with open('./test.txt', 'r+') as read_file:
		text = read_file.readlines()
	read_file.close()

	print(type(text))
