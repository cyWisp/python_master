#!/usr/bin/env python
from sys import argv, exit

def usage(script_name=argv[0]):
	print(f'[!] Usage: {script_name} <DATE>')

def check_args(arg_list):
	if len(arg_list) != 2:
		usage()
		exit(0)
	else:
		if len(arg_list[1]) != 8:
			print(f"[x] Please enter a valid date in the form MMDDYYYY")
			exit(0)
		try:
			int(arg_list[1])
		except ValueError:
			print(f"[x] Please enter a valid date in the form MMDDYYYY")
			exit(0)
		else:
			return arg_list[1]

def calc_dol(digits):

	while len(str(digits)) > 1:
		num_list = [int(x) for x in str(digits)]
		digits = str(sum(list(num_list)))
	else:
		return digits

if __name__ == '__main__':

	date = check_args(argv)
	print(calc_dol(date))

			
			
		
