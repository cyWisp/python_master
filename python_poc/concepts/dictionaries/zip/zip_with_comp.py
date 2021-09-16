#!/usr/bin/env python

if __name__ == '__main__':

	first_names = ["rob", "tom", "lewis"]
	last_names = ["daglio", "johnson", "carroll"]

	full_names = {a:b for a,b in zip(first_names, last_names)}

	print("First Names: ")
	for name in first_names:
		print(name, end=" | ")
	print("\nLast Names: ")
	for name in last_names:
		print(name, end=" | ")
	print("\nFull Names: ")
	for first, last in full_names.items():
		print(f"{first} {last}", end=" | ")
	print("")


