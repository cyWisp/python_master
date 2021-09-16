#!/usr/bin/env python
import sqlite3
from sqlite3 import Error
from queries import (
	CREATE_CONTACTS_TABLE,
	INSERT_CONTACT
)

def create_connection(path):
	db_conn = None
	try: db_conn = sqlite3.connect(path)
	except Error as e: print(f"[x] Error: {e}")
	else:
		print("[+] Connection successful!")
		return db_conn

def execute_query(db_conn, query):
	cursor = db_conn.cursor()
	try:
		cursor.execute(query)
		db_conn.commit()
	except Error as e: print(f"[x] Error: {e}")
	else: print("[+] Query executed successfully!")

def insert_records(db_conn):
	cursor = db_conn.cursor()
	example = ('rob', 'rob@mail.com', '123')
	try:
		cursor.execute(INSERT_CONTACT, example)
		db_conn.commit()
	except Error as e: print(f"[x] Error: {e}")
	else:
		print("[+] Records added successfully!")

if __name__ == '__main__':
	db_conn = create_connection("./test.db")
	execute_query(db_conn, CREATE_CONTACTS_TABLE)


	insert_records(db_conn)

