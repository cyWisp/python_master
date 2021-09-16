#!/usr/bin/env python

class Example:
	def __init__(self):
		self.__var_1 = 3
		self.__string_var = "this is a string"

	def print_vars(self):
		for k, v in self.__dict__.items():
			print(f"{k}: {v}")

if __name__ == '__main__':

	example_1 = Example()

	example_1.print_vars()
	
