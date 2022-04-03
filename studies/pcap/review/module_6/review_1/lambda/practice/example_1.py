#!/usr/bin/env python

if __name__ == '__main__':

	nums = [x for x in range(20)]
	odd = map(lambda x: x if x % 3 == 0, nums)

	print(nums)
