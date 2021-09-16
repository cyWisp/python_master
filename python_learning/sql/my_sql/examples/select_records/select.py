#!/usr/bin/env python
import mysql.connector
from mysql.connector import Error
from getpass import getpass

HOST = '10.0.0.4'
USER = input("User: ")
PASS = getpass("Password: ")
DB_NAME = 'verses'

QUERIES = {
    'get_all_verses': "SELECT * FROM daily_verse;"
}

def connect_db(host, user, passwd, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=db_name
        )
    except Error as e: print(f"[x] Error: {e.__class__.__name__}: {e}")
    else:
        print(f"[*] Connection to {db_name} on {host} successful!")
        return connection

def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Error as e:
        print(f"[x] Error: {e.__class__.__name__}: {e}")
    else:
        print("[*] Query executed successfully!")
        return result

if __name__ == '__main__':
    connection = connect_db(HOST, USER, PASS, DB_NAME)
    result = execute_read_query(connection, QUERIES['get_all_verses'])

    for r in result:
        print(r)