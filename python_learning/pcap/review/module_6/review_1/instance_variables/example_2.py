#!/usr/bin/env python

class ExampleClass:
	def __init__(self, val = 1):
		self.__first = val

	def setSecond(self, val = 2):
		self.__second = val

if __name__ == '__main__':

	# reviewing the output, we see that python adds the class name to any instance
	# variables called from within the class
	# those created outside of the class, so not receive the naming convention

	exampleObject_1 = ExampleClass()
	exampleObject_2 = ExampleClass(2)

	exampleObject_2.setSecond(3)
	
	exampleObject_3 = ExampleClass(4)
	exampleObject_3.__third = 5

	print(exampleObject_1.__dict__)
	print(exampleObject_2.__dict__)
	print(exampleObject_3.__dict__)
	
		
