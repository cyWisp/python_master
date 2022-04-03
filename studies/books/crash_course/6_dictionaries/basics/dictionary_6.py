#!/usr/bin/env python
import os

def main():

	person = {'Name':'Rob','Age':'32','Race':'Hispanic'}

	print('Initial dictionary keys and values:\n')
	print(person)

	print('Modifying name and age...')

	person['Name'] = 'Peter'
	person['Age'] = 12

	print('New values:\n')

	print(person)

if __name__ == '__main__':
	main()
