#!/usr/bin/env python

class Classy:
	""" this is a docstring """

	class_var = 1
	def __init__(self):
		self.instance_var = 2

	def method(self):
		pass

	def __hidden_method(self):
		pass

if __name__ == '__main__':
	obj = Classy()
	
	for k, v in obj.__dict__.items():
		print(f"{k} : {v}")

	print()

	for x, y in Classy.__dict__.items():
		print(f"{x} : {y}")
