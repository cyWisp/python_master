#!/usr/bin/env python
import mysql.connector, json
from mysql.connector import Error
from getpass import getpass

HOST = '10.0.0.4'
USER = input("User: ")
PASS = getpass("Password: ")
DB_NAME = 'verses'
VERSES = "./verses.json"

def get_verses():
    try:
        with open(VERSES, 'r') as f:
            verses = json.load(f)
    except Exception as e:
        print(f"[x] Error: {e.__class__.__name__}: {e}")
    else: return verses

def connect_db(host, user, passwd, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=db_name
        )
    except Error as e:
        print(f"[x] Error: {e.__class__.__name__}: {e}")
    else:
        print(f"[*] Connection to {db_name} on {host} successful!")
        return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f"[x] Error: {e.__class__.__name__}: {e}")
    else:
        print("[*] Query executed successfully!")

def write_to_db(connection, verses):
    for ref, verse in verses.items():
        query = f"""
            INSERT INTO daily_verse (reference, verse) 
            SELECT * FROM (SELECT '{ref}', '{verse}') AS temp 
            WHERE NOT EXISTS (SELECT reference FROM daily_verse WHERE reference='{ref}') LIMIT 1;
        """
        print(query + "\n")
        
        execute_query(connection, query)



if __name__ == '__main__':
    connection = connect_db(HOST, USER, PASS, DB_NAME)
    verses = get_verses()
    write_to_db(connection, verses)

    connection.close()
