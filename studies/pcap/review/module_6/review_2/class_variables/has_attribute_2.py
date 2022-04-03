#!/usr/bin/env python

class ExampleClass:
	attr = 1

if __name__ == '__main__':
	print(hasattr(ExampleClass, 'attr'))
	print(hasattr(ExampleClass, 'prop'))

