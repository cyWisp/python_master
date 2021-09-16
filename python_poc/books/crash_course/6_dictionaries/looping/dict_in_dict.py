#!/usr/bin/env python
import os

def main():

	people = {}
	person = {'Name':'','Age':''}

	count = 0

	while True:

		name = input('Name: ')
		age = input('Age: ')

		person['Name'] = str(name)
		person['Age'] = age

		people['num'] = count
		people['info'] = person

		count = count + 1

		print(people)


	

if __name__ == '__main__':
	main()
