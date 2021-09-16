#!/usr/bin/env python
from random import choice, sample

if __name__ == '__main__':

	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	print(choice(nums))
	print(sample(nums, 5))
	print(sample(nums, 8))
