#!/usr/bin/env python

class Super_Class:
	pass

class Sub_Class(Super_Class):
	pass

if __name__ == '__main__':

	print(issubclass(Super_Class, Sub_Class))
	print(issubclass(Sub_Class, Super_Class))
