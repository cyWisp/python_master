#!/usr/bin/env python
import sqlite3
from sys import exit

def insert_record(name, phone_number, email):

	record = (name, phone_number, email) 

	# Create a connection to the database
	sql_conn = sqlite3.connect('example.db')
	# Create a cursor object
	cursor = sql_conn.cursor()
	
	# Use execute to insert data
	cursor.executemany("INSERT INTO contacts VALUES (?,?,?)", record)

	# commit changes
	sql_conn.commit()
	
	# close the connection
	sql_conn.close()

def gather_data():

	new_record = {'name':'', 'phone':'', 'email':''}
	for i in new_record.keys():
			new_record[i] = input(f'{i}: ')

	return new_record['name'], new_record['phone'], new_record['email']

def run():

	while True:
		sentinel = input("Insert new record? [Y/n]: ")
		if sentinel == 'y':
			user_name, user_phone, user_email = gather_data()
			insert_record(user_name, user_phone, user_email)
		else:
			exit(0)

if __name__ == '__main__':

	run()
