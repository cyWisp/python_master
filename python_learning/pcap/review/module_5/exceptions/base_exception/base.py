#!/usr/bin/env python

if __name__ == '__main__':

	# BaseException -> Exception -> ArithmeticError -> ZeroDivisionError
	
	try:
		q = 3 / 0
	except BaseException as a_error:
		print(f"[x] Error: {a_error}")
	else:
		print(q)
