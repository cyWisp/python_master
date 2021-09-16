#!/usr/bin/env python

def make_adder(n):
	def add(x):
		return x + n
	return add

if __name__ == '__main__':

	plus_3 = make_adder(3)
	plus_5 = make_adder(5)

	add_3 = plus_3(5)
	add_5 = plus_5(5)
	
	print(f"Add 3 plus 5: {add_3}")
	print(f"Add 5 plus 5: {add_5}")
	
