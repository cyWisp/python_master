#!/usr/bin/env python

class ExampleClass:
	def __init__(self, val):
		if val % 2 != 0:
			self.a = 1
		else:
			self.b = 1

if __name__ == '__main__':
	exampleObject = ExampleClass(1)
	print(exampleObject.a)
	print(exampleObject.b)
