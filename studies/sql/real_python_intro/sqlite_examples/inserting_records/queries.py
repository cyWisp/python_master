CREATE_TABLE = """
	CREATE TABLE IF NOT EXISTS contacts (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		email TEXT,
		phone TEXT
	);
"""

INSERT_CONTACT = """
	INSERT INTO
		contacts (name, email, phone)
	VALUES
		('Rob', 'rob@email.com', '123'),
		('Jan', 'jan@mail.com', '222'),
		('Alex', 'alex@mailer.com', '444')
"""
