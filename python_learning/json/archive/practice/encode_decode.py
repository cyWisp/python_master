#!/usr/bin/env python
import json

def encode_data(new_dict, file_name):

	# writing a new file called "./data.json" and dumping the data there
	with open(file_name, "w+") as json_file:
		json.dump(new_dict, json_file)
	json_file.close()



if __name__ == '__main__':

	# Nested dictionary for sample data
	person = {
		"employee": {
			"name": "John",
			"age": "34"	
		}
	}

	# Calling the encode() function
	encode_data(person, "./person.json")

	name_list = ["rob", "bill", "tom"]
	encode_data(name_list, "./name_list.json")



	print("[*] Done...")
	
