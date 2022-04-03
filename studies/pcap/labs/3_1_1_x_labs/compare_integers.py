#!/usr/bin/env python

if __name__ == '__main__':

	num_1 = int(input("First number: "))
	num_2 = int(input("Second number: "))

	if num_1 > num_2:
		print("First is greater!")
	elif num_2 > num_1:
		print("Second is greater!")
	else:
		print("They are equal!")
