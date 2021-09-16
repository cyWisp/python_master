#!/usr/bin/env python
import json

if __name__ == '__main__':

	data = {
		"hostname1": [
			"software item 1",
			"software item 2",
		],
		"hostname2": [
			"software item 1",
			"software item 2",
		],
	}

	with open("sample_data.json", "w") as write_file:
		json.dump(data, write_file)
	write_file.close()
