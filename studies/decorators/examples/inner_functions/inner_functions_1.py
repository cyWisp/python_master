#!/usr/bin/env python

def parent():
	print("Printing from the parent() function")

	def first_child():
		print("Printing from the first_child() function")

	def second_child():
		print("Printing from the second_child() function")

	first_child()
	second_child()

if __name__ == '__main__':
	parent()
