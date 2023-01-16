#!/usr/bin/env python

def shout(text):
	return text.upper() + "!!!"

if __name__ == '__main__':

	insults = ["fuck you", "you suck", "foiled"]

	shouted_insults = list(map(shout, insults))
	[print(x) for x in shouted_insults]
	
