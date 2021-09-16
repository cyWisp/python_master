#!/usr/bin/env python

class Parent:
	def __init__(self):
		self.__privateVar  = 12
	
class Child(Parent):
	def __init__(self):
		Parent.__init__(self)
	
	def print_var(self):
		print(self._Parent__privateVar)

if __name__ == '__main__':

	new_child = Child()

	new_child.print_var()