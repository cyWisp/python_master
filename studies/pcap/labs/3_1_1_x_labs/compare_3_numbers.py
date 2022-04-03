#!/usr/bin/env python

if __name__ == '__main__':

	num_1 = int(input("First number: "))
	num_2 = int(input("Second number: "))
	num_3 = int(input("Third number: "))
	
	largest = num_1

	if num_2 > largest:
		largest = num_2

	if num_3 > largest:
		largest = num_3

	#largest = str(largest)
	print(f"The largest is {largest}")
