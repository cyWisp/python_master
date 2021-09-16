#!/usr/bin/env python
import os

def main():

	print('Starting with an empty dictionary: \n')

	person = {}

	person['Name'] = 'Rob'

	print('Appending an initial key and value:\n')
	print(person)

	person['Age'] = 32
	person['Race'] = 'Hispanic'

	print('Appending two more keys and values:\n')

	print(person)

if __name__ == '__main__':
	main()
