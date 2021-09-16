#!/usr/bin/env python
import sqlite3
from sqlite3 import Error

def create_connection(path):
	db_conn = None
	try:
		db_conn = sqlite3.connect(path)
	except Error as e: print(f"[x] Error: {e}")
	else:
		print("[+] DB Connection success!")
		return db_conn

def execute_read_query(db_conn, query):
	cursor = db_conn.cursor()
	result = None

	try:
		cursor.execute(query)
		result = cursor.fetchall()
	except Error as e: print(f"[x] Error: {e}")
	else:
		print("[+] Query executed successfully!")
		return result

if __name__ == '__main__':
	db_conn = create_connection("./test.db")
	get_all_contacts = "SELECT * FROM contacts;"
	result = execute_read_query(db_conn, get_all_contacts)

	for r in result: print(r)
	
