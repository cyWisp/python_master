#!/usr/bin/env python

def exponents(x):
	def raise_to(n):
		return n ** x
	return raise_to
	

if __name__ == '__main__':

	squared = exponents(2)
	cubed = exponents(3)

	print(squared(2))
	print(cubed(2))

