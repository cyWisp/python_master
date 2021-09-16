#!/usr/bin/env python
import csv

if __name__ == '__main__':

	some_string = """this is just a test string
		to be written to an example csv file.
		it does not contain any significant content
	"""

	try:
		with open('test.csv', 'w+') as test_file:
			test_file.write(some_string)
	except:
		print("[x] Unable to write file...")
	else:
		print("[.] File written!")
	finally:
		test_file.close()

	

