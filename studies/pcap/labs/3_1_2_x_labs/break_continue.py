#!/usr/bin/env python

if __name__ == '__main__':

	# break example
	print("The break instruction")
	for i in range(1, 6):
		if i == 3:
			break
		print("Inside the loop", i)
	print("Outside the loop")

	# continue example
	print("\n\nThe continue instruction")
	for i in range(1, 6):
		if i == 3:
			continue
		print("inside the loop", i)
	print("outside the loop")
