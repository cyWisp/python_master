#!/usr/bin/env python

class ExampleClass:
	a = 1
	def __init__(self):
		self.b = 2

if __name__=='__main__':
	exampleObject = ExampleClass()

	print(hasattr(exampleObject, 'b'))
	print(hasattr(exampleObject, 'a'))
	print(hasattr(ExampleClass, 'b'))
	print(hasattr(ExampleClass, 'a'))
