#!/usr/bin/env python

if __name__ == '__main__':

	try:
		i = int('Hello')
	except Exception as e:
		print(e)
		print(e.__str__())
		print()
		print(e.__dict__)
