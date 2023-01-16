#!/usr/bin/env python

def make_adder(n):
	def add(x):
		return x + n
	return add

if __name__ == '__main__':

	add_3 = make_adder(3)
	add_5 = make_adder(5)

	print(add_3(3))
	print(add_5(3))
	
