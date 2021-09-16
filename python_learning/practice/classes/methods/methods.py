#!/usr/bin/env python

class Test:
	def __init__(self):
		self.name = "test"

	def __str__(self):
		return self.name

if __name__ == '__main__':
	new_test = Test()
	print(new_test)
