#!/usr/bin/env python

if __name__ == '__main__':

	info = {"name": "Tom", "age": 23, "location": "Trention, NJ"}

	location = info.get("location")

	print(f"I live in {location}")

	print(f"Tom's info: ")

	for k, v in info.items():

		print(f"{k}: {v}")
