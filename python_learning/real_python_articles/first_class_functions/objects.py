#!/usr/bin/env python

def yell(text):
	return text.upper() + "!"

if __name__ == '__main__':

	bark = yell
	print(bark("what do you want from me"))

	del yell

	print(bark("'yell' was deleted"))
	print(f"'bark' is still an instance of {bark.__name__}")
	print(f"'bark's qual name is {bark.__qualname__}")
	
