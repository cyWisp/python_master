#!/usr/bin/env python
import json

if __name__ == '__main__':
	try:
		with open("./ci_test.json", 'r') as json_file:
			data = json.load(json_file)
	except Exception as e: print(f"[x] Error: {e}")
	
	for k, v in data.items():
		print(f"{k}", end=": ")
		for i in v:
			if i == v[-1]: print(f"{i}")
			else: print(f"{i}", end=", ")
