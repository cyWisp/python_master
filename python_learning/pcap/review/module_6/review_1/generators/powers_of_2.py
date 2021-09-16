#!/usr/bin/env python

# generator that yields powers of 2 for x
def powersOf2(x):
	pow = 1
	for i in range(x):
		yield pow
		pow *= 2

powers = powersOf2(10)

for x in powers:
	print(x)

# convert the generator into a list

powers_list = [x for x in powersOf2(10)]
print(powers_list)

more_powers = list(powersOf2(10))
print(more_powers)
