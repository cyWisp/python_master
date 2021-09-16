#!/usr/bin/env python
from sys import argv, exit

def usage():
	print(f"[!] Usage: {arg_list[0]} <string>")
def check_args(arg_list):
	if len(arg_list) != 2:
		usage()
		exit(0)
	else:
		if arg_list[1] == "":
			print("[x] String cannot be empty!")
			usage()
			exit(0)
		else:
			return "".join([x for x in arg_list[1] if x != " "])

def test_palindrome(str_var):
	if str_var.upper() == str_var[::-1].upper():
		print("[*] Palindrome")
	else:
		print("[x] Not a palindrome")

if __name__ == '__main__':
	str_var = check_args(argv)
	test_palindrome(str_var)
	
	
