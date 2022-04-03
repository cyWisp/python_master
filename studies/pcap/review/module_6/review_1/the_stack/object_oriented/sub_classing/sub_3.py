#!/usr/bin/env python

class Parent:
	def __init__(self):
		self.__var = list()

	def append_var(self, num):
		self.__var.append(num)

	def print_var(self):
		print(self.__var)

class Child(Parent):
	def __init__(self):
		Parent.__init__(self)
	
	def use_append(self, num):
		Parent.append_var(self, num)

	def use_print(self):
		Parent.print_var(self)

if __name__ == '__main__':

	new_child = Child()

	for i in range(5):
		new_child.use_append(i)

	new_child.use_print()
