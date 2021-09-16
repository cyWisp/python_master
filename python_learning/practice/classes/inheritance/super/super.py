#!/usr/bin/env python

class SuperClass:
	def __init__(self, name):
		self.name = name
		self.test = "test var"
		self.test_2 = "test 2"

	def __str__(self):
		return f"This class is called {self.name}"

class Sub(SuperClass):
	def __init__(self, name):
		super().__init__(name)

	def test_method(self):
		print(f"instance vars: {self.test}\n{self.test_2}")


if __name__ == '__main__':
	obj = Sub("Bob")

	print(obj)
	obj.test_method()
