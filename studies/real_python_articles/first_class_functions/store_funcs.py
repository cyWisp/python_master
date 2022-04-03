#!/usr/bin/env python

def yell(text):
	return text.upper() + "!"

if __name__ == '__main__':

	funcs = [yell, str.lower, str.capitalize]

	for f in funcs:
		print(f)

	print(funcs[0], funcs[0]("hi there"))
