#!/usr/bin/env python

def make_mult(n):
	def mult(x):
		return n * x
	return mult

if __name__ == '__main__':

	times_2 = make_mult(2)
	times_3 = make_mult(3)
	
	print(times_2(6))
	print(times_3(5))
	
