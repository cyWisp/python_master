#!/usr/bin/env python

class Test_1:
	def __init__(self):
		self.var_1 = "this is the first var"
		self.var_2 = 4

	def print_vars(self):
		for i in self.__dict__.values():
			print(str(i))

class Test_2(Test_1):
	def __init__(self):
		Test_1.__init__(self)

	def print_vars(self):
		Test_1.print_vars(self)

if __name__ == '__main__':

	tester = Test_1()
	tester.print_vars()

	tester_2 = Test_2()

	tester_2.print_vars()
