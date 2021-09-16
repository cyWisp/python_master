#!/usr/bin/env python

class ExampleClass:
	varia = 1
	def __init__(self, val):
		ExampleClass.varia = val

if __name__ == '__main__':
	print(ExampleClass.__dict__)
	
	exampleObject = ExampleClass(2)
	
	print(ExampleClass.__dict__)
	print(exampleObject.__dict__)
