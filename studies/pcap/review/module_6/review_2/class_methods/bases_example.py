#!/usr/bin/env python

class SuperOne:
	pass

class SuperTwo:
	pass

class Sub(SuperOne, SuperTwo):
	pass

def printBases(cls):
		print('( ', end='')

		for x in cls.__bases__:
			print(x.__name__, end=' ')
		print(')')

		print()

if __name__ == '__main__':
	printBases(SuperOne)
	printBases(SuperTwo)
	printBases(Sub)
