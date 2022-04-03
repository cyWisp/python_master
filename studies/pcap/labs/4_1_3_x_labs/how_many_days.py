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

def days_in_month(year, month):

	leap_year = is_leap_year(year)

	months_and_days = {
		1:31, 
		2:28, 
		3:31, 
		4:30, 
		5:31, 
		6:30, 
		7:31, 
		8:31, 
		9:30, 
		10:31,
		11:30,
		12:31,
	}
	
	if leap_year:
		months_and_days[2] = 29
	else:
		pass

	return months_and_days[month]

if __name__ == '__main__':

	test_years = [1900, 2000, 2016, 1987]
	test_months = [2, 2, 1, 11]
	test_results = [28, 29, 31, 30]

	for i in range(len(test_years)):
		yr = test_years[i]
		mo = test_months[i]

		print(yr, mo, "-> ", end="")
		result = days_in_month(yr, mo)
		if result == test_results[i]:
			print(f"{result}: OK")
		else:
			print(f"{result}: Failed!")
		


