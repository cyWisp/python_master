#!/usr/bin/env python
import os, sqlite3

db_file_name = './todo.db'

# Will default to True if db_file_name does not exist
db_is_new = not os.path.exists(db_file_name)

db_connection = sqlite3.connect(db_file_name)

if db_is_new: # (is True)
	print('[!] Schema not yet defined!')
else:
	print('[!] Database exists. | Assume schema does as well.')

db_connection.close()
	
