#!/usr/bin/env python
from decorators import deco

@deco
def say_hi(name):
	print(f"hi {name}")

@deco
def say_something():
	print("something")

if __name__ == '__main__':
	say_hi("bob")
	say_something()
