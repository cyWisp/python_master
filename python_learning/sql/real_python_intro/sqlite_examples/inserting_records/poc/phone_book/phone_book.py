#!/usr/bin/env python
from menu import main_menu
from common import DB_PATH
from db import connect, execute_query
from queries import CREATE_CONTACTS_TABLE

def op(choice):
	if choice == "1":
		print("you picked 1")

if __name__ == '__main__':
	choice = main_menu()
	db_conn = connect(DB_PATH)
	execute_query(db_conn, CREATE_CONTACTS_TABLE)
	op(choice)
