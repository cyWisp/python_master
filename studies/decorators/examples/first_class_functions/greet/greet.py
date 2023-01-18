#!/usr/bin/env python

def say_hello(name):
	return f"Hello, {name}"

def be_awesome(name):
	return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func, name):
	return greeter_func(name)

if __name__ == '__main__':
	print(greet_bob(say_hello, "bob"))
	print(greet_bob(be_awesome, "bob"))
