#!/usr/bin/env python
from decorators import do_twice

@do_twice
def say_something():
	print("this is something")

if __name__ == '__main__':
	say_something()
