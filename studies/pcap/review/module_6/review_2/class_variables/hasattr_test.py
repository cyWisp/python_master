#!/usr/bin/env python

class ExampleClass:
	def __init__(self):
		self.a = "this"
		self.b = "that"

if __name__ == '__main__':
	exampleObject = ExampleClass()

	print(hasattr(exampleObject, 'a'))
