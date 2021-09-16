#!/usr/bin/env python
import sqlite3
from sqlite3 import Error
from queries import (
	CREATE_CONTACTS_TABLE,
	ADD_CONTACT
)
from sys import exit

def create_connection(path):
	db_conn = None
	try:
		db_conn = sqlite3.connect(path)
	except Error as e: print(f"[x] Error: {e}")
	else:
		print("[+] Connection successful!")
		return db_conn

def execute_query(db_conn, query, data=None):
	cursor = db_conn.cursor()
	try:
		if not data:
			cursor.execute(query)
			db_conn.commit()
		else:
			cursor.execute(query, data)
			db_conn.commit()
	except Error as e: print(f"[x] Error: {e}")
	else: print("[+] Query executed successfully!")

def add_contacts(db_conn, query):
	print("[!] Adding contacts- type 'end' to quit the program...")
	name, email = None, None
	while True:
		if name == "end" or email == "end":
			print("[!] Exiting...")
			exit() 
		name = input("[?] Name: ")
		email = input("[?] Email: ")
		new_record = (name, email)
		
		print("[+] Appending new record to database...")
		execute_query(db_conn, query, new_record)
		
if __name__ == '__main__':
	db_conn = create_connection("./test.db")
	execute_query(db_conn, CREATE_CONTACTS_TABLE)
	add_contacts(db_conn, ADD_CONTACT)
