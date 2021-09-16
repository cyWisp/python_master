#!/usr/bin/env python
import sqlite3
from sqlite3 import Error

def connect(path):
	db_conn = None
	try:
		db_conn = sqlite3.connect(path)
	except Error as e: print("[x] Error: {e}")
	else:
		print("[+] DB connection successful!")
		return db_conn

def execute_query(db_conn, query):
	cursor = db_conn.cursor()
	try:
		cursor.execute(query)
		db_conn.commit()
	except Error as e: print("[x] Error: {e}")
	else: print("[+] Query executed successfully!")


	
