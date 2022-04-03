#!/usr/bin/env python

class Classy:
	pass

if __name__ == '__main__':

	print(Classy.__module__)
	obj = Classy()
	print(obj.__module__)
