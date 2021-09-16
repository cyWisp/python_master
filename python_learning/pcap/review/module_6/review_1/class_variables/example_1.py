#!/usr/bin/env python

class ExampleClass:
	counter = 0
	def __init__(self, val = 1):
		self.__first = val
		ExampleClass.counter += 1

if __name__ == '__main__':

	# class variables are declared outside of the constructor
	# class variables are contained within the class itself

	exampleObject_1 = ExampleClass()
	exampleObject_2 = ExampleClass(2)
	#exampleObject_3 = ExampleClass(4)

	print(exampleObject_1.__dict__, exampleObject_1.counter)
	print(exampleObject_2.__dict__, exampleObject_2.counter)
	#print(exampleObject_3.__dict__, exampleObject_3.counter)
