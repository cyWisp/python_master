#!/usr/bin/env python
from sys import exit

def test():
	while True:
		try:
			x = int(input("Enter a non-negative value: "))
			assert x >= 0
		except (ValueError, AssertionError):
			print("[x] Please enter a valid non-negative number...")
		else:
			print(f"Nunmber: {x}")
			break
	

if __name__ == '__main__':	

	test()
	print("End..")
	
