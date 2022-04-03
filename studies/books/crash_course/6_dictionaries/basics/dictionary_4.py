#!/usr/bin/env python
import os

def main():

	print('Print the initial dictionary:\n')

	person = {'Name':'Rob'}
	print(str(person) + '\n')

	print('Append two new keys and values:\n')

	person['Age'] = 32
	person['Race'] = 'Hispanic'

	print(person)
	


if __name__ == '__main__':
	main()
