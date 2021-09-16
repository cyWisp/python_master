#!/usr/bin/env python

def make_greeter(text):
	def say_hi():
		return "hi there, " + text
	return say_hi


if __name__ == '__main__':

	hi_rob = make_greeter("rob")
	print(hi_rob())
	
