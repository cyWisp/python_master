#!/usr/bin/env python
import os

###########################################
# title: check.py
# purpose: input validation
# author: wisp
# date: 08/28/2018
###########################################


if __name__ == '__main__':

	symbols = ",./;'[]\-=`!@#$%^&*()_+{}|:<>?~ "
	numbers = "1234567890"
	letters = "abcdefghijklmnopqrstuvwxyz"
	cap_letters = []

	for letter in letters:
		cap = letter.upper()
		cap_letters.append(cap)

	check = input("check: ")
	
	for symbol in symbols:
		for i in check:
			if i in symbols:
				print("entry contains symbols")
				break
			else:
				pass
		break

	for number in numbers:
		for i in check:
			if i in numbers:
				print("entry contains numbers")
				break
			else:
				pass
		break

	for letter in letters:
		for i in check:
			if i in letters or i in cap_letters:
				print("entry contains letters")
				break
			else:
				pass
		break
