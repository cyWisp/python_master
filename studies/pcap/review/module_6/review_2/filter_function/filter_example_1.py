#!/usr/bin/env python
from random import seed, randint

if __name__ == '__main__':

	seed()
	data = [randint(-10, 10) for x in range(5)]
	filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

	print(f"{data}\n{filtered}")
