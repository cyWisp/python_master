import logging
import psycopg2
import sys
from psycopg2 import OperationalError, Error

logging.basicConfig(
    format='%(process)d - %(asctime)s - %(filename)s - '
           '%(funcName)s - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)

log = logging.getLogger()

# Example Queries
CREATE_USER_TABLE = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL, 
        age INTEGER,
        location TEXT
    )
'''

INSERT_USER = '''
    INSERT INTO users (
        name, age, location
    ) VALUES (%s, %s, %s);
'''


class PDB:
    RETRIES = 3

    def __init__(
        self,
        db_name: str,
        db_user: str,
        db_pass: str,
        db_host: str,
        db_port: int
    ) -> None:
        self.db_name = db_name
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_host = db_host
        self.db_port = db_port

        self.connection, self.cursor = None, None

    def connect(self):
        for r in range(self.RETRIES):
            if not self.connection:
                try:
                    log.info(f'Connecting to database. Attempt {r + 1}')

                    self.connection = psycopg2.connect(
                        database=self.db_name,
                        user=self.db_user,
                        password=self.db_pass,
                        host=self.db_host,
                        port=self.db_port
                    )
                    self.connection.autocommit = True

                    log.info('Connection successful.')

                    if r == self.RETRIES - 1:
                        raise OperationalError

                except OperationalError as e:
                    log.error(f'Unable to connect to database:\n{e}')
                    sys.exit()

    def __str__(self):
        return vars(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

    def check_connection(self):
        if not self.connection:
            self.connect()

        if not self.cursor:
            self.cursor = self.connection.cursor()

    def run_query(self, query: str):
        try:
            log.info(f'Running {query}')

            self.check_connection()
            self.cursor.execute(query)

            log.info(f'Execution successful.')

        except OperationalError as e:
            log.error(e)

    def insert(self, data: list):
        self.check_connection()

        try:
            for i in data:
                log.info(f'Executing: {INSERT_USER} | Data: {i}\n')
                self.cursor.execute(INSERT_USER, i)

        except (OperationalError, Error) as e:
            log.error(f'Unable to perform insert operation '
                      f'on database:\n{e}', exc_info=True)


if __name__== '__main__':
    from user_generator import Users

    log.info('Init.')

    with Users() as u:
        new_users = u.generate_users(1000)

    with PDB(
        db_name='testdb',
        db_user='test',
        db_pass='password',
        db_host='localhost',
        db_port=5432
    ) as db:
        db.run_query(CREATE_USER_TABLE)
        db.insert(new_users)


        # db.insert([('Sammy', '12', 'Portland, OR')])
