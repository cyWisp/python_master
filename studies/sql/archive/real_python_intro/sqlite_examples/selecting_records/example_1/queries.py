CREATE_CONTACTS_TABLE = """
	CREATE TABLE IF NOT EXISTS contacts (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		email TEXT,
		phone TEXT
	);
"""

INSERT_CONTACT = """
	INSERT INTO
		contacts(name, email, phone)
		values(?, ?, ?);
"""

