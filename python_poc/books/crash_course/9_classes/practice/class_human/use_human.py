#!/usr/bin/env python
import os, human

def main():

	friend = human.Human('Rob', 32)
	salutation = 'Hi there, '

	friend.introduction(salutation)
	friend.say_age()

if __name__ == '__main__':
	main()
