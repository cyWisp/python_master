#!/usr/bin/env python

if __name__ == '__main__':

	e = "somone@mail.com"
	for x in e:
		if x == "@":
			break
		else:
			print(x, end="")
	print()
