#!/usr/bin/env python

def is_leap_year(year):

	if (year % 4) == 0 and (year % 100) == 0 and (year % 400) == 0:
		return True
	elif (year % 4) == 0 and (year % 100) == 0 and (year % 400) != 0:
		return False
	elif (year % 4 == 0) and (year % 100) != 0:
		return True
	else:
		return False

if __name__ == '__main__':

	test_data = [1900, 2000, 2016, 1987]
	test_results = [False, True, True, False]

	for index, item in enumerate(test_data):
		result = is_leap_year(item)
		print(f"Year: {item} | ", end="")
		if result == test_results[index]:
			print("OK")
		else:
			print("Failed")

	
