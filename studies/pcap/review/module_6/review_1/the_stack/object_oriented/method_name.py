#!/usr/bin/env python

class This_Class:
	def __init__(self):
		pass
	def this_method(self):
		print(self.__name__)

if __name__ == '__main__':

	new_class = This_Class()
	new_class.this_method()
