#!/usr/bin/env python

if __name__ == '__main__':

	year = int(input("Year: "))
	year_type = ""	

	if year < 1582:
		print("Not within the Gregorian calendar period...")
	elif (year % 4) != 0:
		year_type = "Common Year"
		print(f"Year: {year} | Type: {year_type}")
	elif (year % 100) != 0:
		year_type = "Leap Year"
		print(f"Year: {year} | Type: {year_type}")
	elif (year % 400) != 0:
		year_type = "Common Year"
		print(f"Year: {year} | Type: {year_type}")
	else:
		year_type = "Leap year"
		print(f"Year: {year} | Type: {year_type}")

	
	
