#!/usr/bin/env python

class Super:
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return f"My name is {self.name}"

class Sub(Super):
	def __init__(self, name):
		Super.__init__(self, name)

if __name__ == '__main__':
	obj = Sub("Andy")
	print(obj)
