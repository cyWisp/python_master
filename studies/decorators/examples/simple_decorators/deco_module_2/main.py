#!/usr/bin/env python
from decorators import add_stuff

@add_stuff
def some_func():
	print("this is the regular func")

if __name__ == '__main__':
	some_func()
