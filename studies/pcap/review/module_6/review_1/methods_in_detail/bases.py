#!/usr/bin/env python
"""
	__bases__ is a tuple. the tuple contains clases (not class names) which are direct superclasses 	for the class.
"""

class SuperOne:
	pass

class SuperTwo:
	pass

class Sub(SuperOne, SuperTwo):
	pass

def printBases(cls):
	print('( ', end='')

	for x in cls.__bases__:
		print(x.__name__, end='')
	print(')')

if __name__ == '__main__':

	printBases(SuperOne)
	printBases(SuperTwo)
	printBases(Sub)
