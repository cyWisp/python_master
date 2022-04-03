#!/usr/bin/env python

class Classy:
	pass

if __name__ == '__main__':
	print(Classy.__name__)

	obj = Classy()
	print(type(obj).__name__)
