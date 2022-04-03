#!/usr/bin/env python

class Classy:
	def visible(self):
		print("visible")

	def __hidden(self):
		print("hidden")

if __name__ == '__main__':

	obj = Classy()
	obj.visible()

	try:
		obj.__hidden()
	except:
		print("failed")

	obj._Classy__hidden()
	
