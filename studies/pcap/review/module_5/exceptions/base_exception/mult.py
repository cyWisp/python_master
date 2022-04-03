#!/usr/bin/env python

if __name__ == '__main__':

	try:
		x = 4 / 0
	except (ZeroDivisionError, ArithmeticError) as e:
		print(f"Error: {e}")
	else:
		print(x)
