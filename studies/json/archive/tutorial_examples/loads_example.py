#!/usr/bin/env python
import json

if __name__ == '__main__':


	with open("./data_file.json", "r") as data_file:

		new_json_object = json.load(data_file)

	data_file.close()		


	print(type(new_json_object))
