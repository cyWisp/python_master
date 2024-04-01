#!/usr/bin/env python
import mysql.connector, getpass
from mysql.connector import Error

HOST = '10.0.0.4'
USER = input("[?] User: ")
PASS = getpass.getpass("[?] Password: ")
DB_NAME = 'verses'
DAILY_VERSE_TABLE = 'daily_verse'

QUERIES = {
    'get_all_verses': f"SELECT * FROM {DAILY_VERSE_TABLE};"
}

def connection(host, user, passwd, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=db_name
        )
    except Error as e: print(f"[x] Error: {e.__class__.__name__}")
    else:
        print(f"[*] Connection to {db_name} on {host} successful!")
        return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e: print(f"[x] Error: {e.__class__.__name__}: {e}")
    else:
        print("[*] Query executed successfully!")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Error as e: print(f"[x] Error: {e.__class__.__name__}: {e}")
    else:
        print("[*] Query executed successfully!")
        return result

if __name__ == '__main__':
    connection = connection(HOST, USER, PASS, DB_NAME)
    initial = execute_read_query(connection, QUERIES['get_all_verses'])
    
    print()
    for i in initial:
        print(i)
    
    update_verse = """
        UPDATE daily_verse
        SET
        reference = "Psalm 127:1",
        verse = "Except the Lord build the house, they labour in vain that build it."
        WHERE
            reference = "John 3:16";
    """

    print()
    execute_query(connection, update_verse)

    print()
    ending = execute_read_query(connection, QUERIES['get_all_verses'])

    for e in ending:
        print(e)

    connection.close()
