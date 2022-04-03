#!/usr/bin/env python

class Classy:
	def __init__(self, value = None):
		self.var = value

if __name__ == '__main__':
	object_1 = Classy("object")
	object_2 = Classy()

	print(object_1.var)
	print(object_2.var)
