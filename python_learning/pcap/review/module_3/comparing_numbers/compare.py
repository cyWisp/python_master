#!/usr/bin/env python

if __name__== '__main__':

	nums = [int(input("Num: ")) for x in range(3)]
	l = 0

	for x in nums:	
		if x > l: l = x
		else: continue
		
	print(l)
