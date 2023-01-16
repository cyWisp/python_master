#!/usr/bin/env python
import sqlite3
from sqlite3 import Error


# Create tables
CREATE_USERS_TABLE = """
	CREATE TABLE IF NOT EXISTS users(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		age INTEGER NOT NULL,
		gender TEXT,
		nationality TEXT
	);
"""

CREATE_POSTS_TABLE = """
	CREATE TABLE IF NOT EXISTS posts(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		title TEXT NOT NULL,
		description TEXT NOT NULL,
		user_id INTEGER_NOT_NULL,
		FOREIGN KEY (user_id) REFERENCES users (id)
	);
"""

CREATE_COMMENTS_TABLE = """
	CREATE TABLE IF NOT EXISTS comments (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		text TEXT NOT NULL,
		user_id INTEGER NOT NULL,
		post_id INTEGER NOT NULL,
		FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
	);
"""

CREATE_LIKES_TABLE = """
	CREATE TABLE IF NOT EXISTS likes (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		user_id INTEGER NOT NULL,
		post_id INTEGER NOT NULL,
		FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
	);
"""

# Insert records
CREATE_USERS = """
	INSERT INTO
		users (name, age, gender, nationality)
	VALUES
		('James', 25, 'male', 'USA'),
		('Leila', 32, 'female', 'France'),
		('Brigitte', 35, 'female', 'England'),
		('Mike', 40, 'male', 'Denmark'),
		('Elizabeth', 21, 'female', 'Canada');
"""

CREATE_POSTS = """
	INSERT INTO
		posts (title, description, user_id)
	VALUES
		("Happy", "I am feeling very happy today", 1),
		("Hot Weather", "The weather is very hot today", 2),
		("Help", "I need some help with my work", 2),
		("Great News", "I am getting married", 1),
		("Interesting Game", "It was a fantastic game of tennis", 5),
		("Party", "Anyone up for a late-night party today?", 3);
"""

CREATE_COMMENTS = """
	INSERT INTO
		comments (text, user_id, post_id)
	VALUES
		('Count me in', 1, 6),
		('What sort of help?', 5, 3),
		('Congrats buddy', 2, 4),
		('I was rooting for Nadal though', 4, 5),
		('Help with your thesis?', 2, 3),
		('Many congratulations', 5, 4);
"""

CREATE_LIKES = """
	INSERT INTO
		likes (user_id, post_id)
	VALUES
		(1, 6),
		(2, 3),
		(1, 5),
		(5, 4),
		(2, 4),
		(4, 2),
		(3, 6);
"""

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
	else: print("[+] Query successful!")

def execute_read_query(db_conn, query):
	cursor = db_conn.cursor()
	result = None
	try:
		cursor.execute(query)
		result = cursor.fetchall()
	except Error as e: print(f"[x] Error reading database: {e}")
	else:
		print("[+] Data read successfully...")
		return result

if __name__ == '__main__':
	# Create a connection to the database
	db_conn = create_connection("./test.db")

	# Create tables
	execute_query(db_conn, CREATE_USERS_TABLE)
	execute_query(db_conn, CREATE_POSTS_TABLE)
	execute_query(db_conn, CREATE_COMMENTS_TABLE)
	execute_query(db_conn, CREATE_LIKES_TABLE)

	# Insert records
#	execute_query(db_conn, CREATE_USERS)
#	execute_query(db_conn, CREATE_POSTS)
#	execute_query(db_conn, CREATE_COMMENTS)
#	execute_query(db_conn, CREATE_LIKES)

	# Select records
	select_users = "SELECT * FROM users;"
	
	users = execute_read_query(db_conn, select_users)
	
	print("[+] Users:")
	for user in users:
		print(user)
	print()

	select_posts = "SELECT * FROM posts;"
	posts = execute_read_query(db_conn, select_posts)
	
	print("[+] Posts")
	for post in posts:
		print(post)
	print()

	# Select using JOIN
	select_users_posts = """
		SELECT
			users.id,
			users.name,
			posts.description
		FROM
			posts
			INNER JOIN users ON users.id = posts.user_id		
	"""
	users_posts = execute_read_query(db_conn, select_users_posts)
	
	print("[+] Users' posts:")
	for users_post in users_posts:
		print(users_post)
	print()
