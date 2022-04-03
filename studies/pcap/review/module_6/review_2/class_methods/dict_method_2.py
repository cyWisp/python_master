#!/usr/bin/env python

class Classy:
	varia = 1
	def __init__(self):
		self.var = 2

	def method(self):
		pass

	def __hidden(self):
		print("this is a hidden method...")

if __name__ == '__main__':
	obj = Classy()

	print(f"{obj.__dict__}\n")
	
	for k, v in Classy.__dict__.items():
		print(f"{k}: {v}")

	print("\n")
	obj._Classy__hidden()
