#!/usr/bin/env python

class Classy:
	def __init__(self):
		self.__var = "hidden"

if __name__ == '__main__':
	obj = Classy()
	print(obj._Classy__var)
