#!/usr/bin/env python
import sqlite3, os
from sqlite3 import Error

CREATE_TABLE = """
	CREATE TABLE IF NOT EXISTS users (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		age INTEGER,
		gender TEXT,
		nationality TEXT
	);
"""

def check_db_exists(path):
	if os.path.exists(path): print("[+] Database exists...")
	else: print("[+] Database does not exist. Creating...")

def close_connection(db_conn):
	print("[+] Closing database connection...")
	db_conn.close()

def create_connection(path):
	check_db_exists(path)
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
	except Error as e: print("[x] Error: {e}")
	else: 
		print("[+] Query executed successfully!")

if __name__ == '__main__':
	db_conn = create_connection("./test.db")
	execute_query(db_conn, CREATE_TABLE)
	close_connection(db_conn)
	
