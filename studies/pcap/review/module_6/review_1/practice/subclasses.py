#!/usr/bin/env python

class Super:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f"My name is {self.name}"

	def greet(self):
		return f"Hi there, my name is {self.name}, what's yours?"

class Sub(Super):
	def __init__(self, name):
		Super.__init__(self, name)

if __name__ == '__main__':
	

	object_1 = Sub("Rob")
	print(object_1)
	print(object_1.greet())
	print(Super.__subclasses__())
