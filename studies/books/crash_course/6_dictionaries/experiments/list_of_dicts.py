#!/usr/bin/env python
import os

def main():

	person_1 = {'Name':'Rob D','Age':'32','Race':'Hispanic'}
	person_2 = {'Name':'Evert C.','Age':'32','Race':'Caucasian'}
	person_3 = {'Name':'Rob A.','Age':'42','Race':'Caucasian'}

	people = [person_1, person_2, person_3]

	for person in people:
		print(str(person) + '\n')

if __name__ == '__main__':
	main()
