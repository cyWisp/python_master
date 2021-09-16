#!/usr/bin/env python
import os

def main():

	record_list = []
	record_dict = {}

	num_records = int(input('How many records?: '))

	for record in range(0, num_records):
		record_dict['Name'] = input('Name: ')
		record_dict['Age'] = input('Age: ')

		record_list.append(record_dict)
		record_dict = {}

	print('\n\n')

	for entry in record_list:
		for key, value in entry.items():
			print('{}: {}\n'.format(key, value))
	

if __name__ == '__main__':
	main()
