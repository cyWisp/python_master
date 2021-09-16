#!/usr/bin/env python
import json

if __name__ == '__main__':

	data = {
		"president": {
			"name": "Donald Trump",
			"species": "human"
		}
	}

	# Writing to a file with json.dump()
	with open("data_file.json", "w+") as new_json_file:
		json.dump(data, new_json_file)

	new_json_file.close()

	# Writing to an object with json.dump()
	new_json_object = json.dumps(data)


	print(new_json_object)

		

