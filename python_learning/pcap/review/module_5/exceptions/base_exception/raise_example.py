#!/usr/bin/env python

def bad_fun(n):
	try:
		return n / 0
	except:
		print("something went wrong")
		raise

def bad_fun_2(x):
	return x / 0

if __name__ == '__main__':

	try:
		bad_fun_2(0)
	except ArithmeticError:
		print("indeed, something did")

	print ("end")

