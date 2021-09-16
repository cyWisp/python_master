#!/usr/bin/env python

class Super:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f"my name is {self.name}"

	def greet(self):
		return f"I'm {self.name}, what's your name?"

class Sub(Super):
	def __init__(self, name):
		Super.__init__(self, name)

if __name__ == '__main__':

	ob1 = Sub("Rob")

	print(ob1)
	print(ob1.greet())
