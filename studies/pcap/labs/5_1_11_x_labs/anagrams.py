#!/usr/bin/env python
from sys import argv, exit

def usage(script_name):
	print(f"[!] Usage: {script_name} <string_1> <string_2>")

def check_args(arg_list):
	if len(arg_list) != 3:
		usage(arg_list[0])
		exit(0)
	else:
		return "".join([x for x in arg_list[1] if x != " "]).upper(), "".join([y for y in arg_list[2] if y != " "]).upper()

def check_anagram(first_string, second_string):
	first_list, second_list = "".join(sorted(list(first_string))), "".join(sorted(list(second_string)))
	if first_list == second_list:
		print("[*] Anagrams")
	else:
		print("[x] Not anagrams")

if __name__ == '__main__':

	first_string, second_string = check_args(argv)
	check_anagram(first_string, second_string)
