#!/usr/bin/env python

class Base:
	def __init__(self):
		self.__var_1 = 5

	def print_var(self):
		print(self.__var_1)


class Derived(Base):
	def __init__(self):
		Base.__init__(self)

	def print_var(self):
		Base.print_var(self)

if __name__ == '__main__':

	b = Base()
	d = Derived()

	# raises an attribute error
	# print(b.__var)

	b.print_var()
	d.print_var()


