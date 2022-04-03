#!/usr/bin/env python

class ExampleClass:
	def __init__(self, val = 1):
		self.first = val

	def setSecond(self, val):
		self.second = val

if __name__ == '__main__':

	# The __dict__ variable contains a list of the class's variables

	new_class_1 = ExampleClass()
	new_class_2 = ExampleClass(3)

	new_class_1.setSecond(5)
	new_class_2.setSecond(12)

	print(f"new_class_1: {new_class_1.__dict__}")
	print(f"new_class_2: {new_class_2.__dict__}")
