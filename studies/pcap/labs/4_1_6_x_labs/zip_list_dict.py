#!/usr/bin/env python

if __name__ == '__main__':

	names = ["rob", "fred", "alex"]
	ages = ["33", "44", "32"]

	names_and_ages = dict(zip(names, ages))

	for k, v in names_and_ages.items():
		print(f"{k}: {v}")
