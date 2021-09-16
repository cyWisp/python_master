#!/usr/bin/env python

if __name__ == '__main__':

	nums = [x for x in range(10)]
	odds = list(map(lambda x: x if x % 3 == 0 else None, nums))

	for i in odds:
		if i != None: print(i, end=' ')
		else: continue
	print()
