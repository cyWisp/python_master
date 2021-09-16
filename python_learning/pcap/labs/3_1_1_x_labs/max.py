#!/usr/bin/env python

from random import randint

if __name__ == '__main__':

	random_numbers = [randint(1, 30) for x in range(30)]
	[print(y) for y in random_numbers]
	print(f"\n Max = {max(random_numbers)}\nMin = {min(random_numbers)}\nAverage = {avg(random_number)}")
