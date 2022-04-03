#!/usr/bin/env python

if __name__ == '__main__':
	try:
		i = int('hi there')
	except Exception as e:
		print(e)
		print(e.__str__())
