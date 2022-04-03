#!/usr/bin/env python
import os

def main():

	list_1 = []
	dict_  = {'Name':'','Age':'','Location':''}	


	num_records = input('How many records: ')

	for records in range(0, int(num_records)):
		
		dict_1['Name'] = input('Name: ')
		dict_1['Age'] = input('Age: ')
		dict_1['Location'] = input('Location: ')

		list_1.append(dict_1)	

	print('\n\n\n')

	print(str(list_1))

#
#	for person in list_1:
#		for key, value in dict_1.items():
#			print('{}: {}'.format(key, value))
			
	
	
if __name__ == '__main__':
	main()
