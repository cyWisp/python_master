#!/usr/bin/env python
from decorators import do_twice

@do_twice
def greet(name):
	print(f"hi {name}")

@do_twice
def say_something():
	print("something")

if __name__ == '__main__':

	greet("rob")
	say_something()
