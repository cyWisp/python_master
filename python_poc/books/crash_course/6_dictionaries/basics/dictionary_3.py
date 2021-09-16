#!/usr/bin/env python
import os

def main():

	person = {'Name':'Rob','Age':'32','Race':'Hispanic'}

	new_age = person['Age']

	print("Hi {}, I know that you're {}, and that you're {} years old!".format(person['Name'], person['Race'], new_age))

if __name__ == '__main__':
	main()
