#!/usr/bin/env python
FILE_NAME = "./test_file.txt"

def generate_content(file_name):
	try:
		with open(file_name, 'rt') as input_file:
			content = [x.strip("\n") for x in input_file.readlines()]
	except Exception as e: print(f"Something went wrong: {e}")
	finally: input_file.close()

	return content

if __name__ == '__main__':
	for i in generate_content(FILE_NAME): print(i)	
