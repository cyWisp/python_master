#!/usr/bin/env python

class Adder:
	def __init__(self, n):
		self.n = n
	def __call__(self, x):
		return self.n + x

if __name__ == '__main__':
	
	plus_3 = Adder(3)
	print(plus_3(4))

	print(callable(plus_3))
