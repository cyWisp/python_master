#!/usr/bin/env python
import json

if __name__ == '__main__':

	with open("./alpha.txt", "r+") as data_file:
		data = json.load(data_file)

	with open("./alpha.json", "w+") as out_file:
		json.dump(data, out_file)
