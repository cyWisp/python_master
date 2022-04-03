#!/usr/bin/env python

class Tester:
	def __init__(self, var_1, var_2):
		self.var_1 = var_1
		self.var_2 = var_2

	def __enter__(self):
		return self

	def __exit__(self):
		return self

	def print_vars(self):
		print("var1: ", self.var_1)
		print("var2: ", self.var_2)

if __name__ == '__main__':
	with Tester("rob", 34) as new_tester:
		new_tester.print_vars()
