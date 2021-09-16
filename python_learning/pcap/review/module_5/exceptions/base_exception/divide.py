#!/usr/bin/env python

if __name__ == '__main__':
	
	try:
		num_1 = int(input("Dividend: "))
		num_2 = int(input("Divisor: "))
	except BaseException as e:
		print(f"[x] Error: {e}")
	else:
		print(str(num_1/num_2))
	
