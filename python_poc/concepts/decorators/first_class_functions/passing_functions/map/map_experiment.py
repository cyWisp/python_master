#!/usr/bin/env python

def greet_people(name):
	return f"Hello {name}- how are you?"

if __name__ == '__main__':

	friends = ["mike", "tom", "bill"]
	say_hi = list(map(greet_people, friends))
	[print(x) for x in say_hi]

	
