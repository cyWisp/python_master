#!/usr/bin/env python
import sqlite3
from sqlite3 import Error
from queries import CREATE_USERS_TABLE

# Create a connection to the database
def create_connection(path):
    connection = None
    try: connection = sqlite3.connect(path)
    except Error as e: print(f"[x] Error: {e}")
    else:
        print("[+] Connection successful...")
        return connection


def execute_query(db_conn, query):
    cursor = db_conn.cursor()
    try:
        cursor.execute(query)
        db_conn.commit()
    except Error as e: print(f"[x] Error: {e}")
    else: print("[+] Query executed successfully...")


if __name__ == '__main__':
    # Connect to the database
    db_conn = create_connection("./test.db")
    
    # Execute CREATE_USERS_TABLE query
    execute_query(db_conn, CREATE_USERS_TABLE)