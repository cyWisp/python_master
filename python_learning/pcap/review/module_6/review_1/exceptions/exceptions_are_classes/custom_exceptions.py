#!/usr/bin/env python

class MyZeroDivisionError(ZeroDivisionError):
	pass

def doTheDivision(mine):
	if mine:
		raise MyZeroDivisionError("some worse news")
	else:
		raise ZeroDivisionError("some bad news")

if __name__ == '__main__':
	for mode in [False, True]:
		try:
			doTheDivision(mode)
		except ZeroDivisionError:
			print("Dividing by zero not allowed")

	for mode in [False, True]:
		try:
			doTheDivision(mode)
		except MyZeroDivisionError:
			print("My division by zero error")
		except ZeroDivisionError:
			print("Original division by zero error")
