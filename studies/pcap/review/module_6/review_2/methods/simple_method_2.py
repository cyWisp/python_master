#!/usr/bin/env python

class Classy():
	def __init__(self, name):
		self.name = name

	def greet(self, intro):
		print(f"{intro} {self.name}")

if __name__ == '__main__':
	exampleObject = Classy('Rob')
	exampleObject.greet("Hi, my name is")
