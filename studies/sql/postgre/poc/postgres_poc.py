import logging
import psycopg2
import json
from random import choice, randint

from enum import Enum
from psycopg2 import OperationalError


logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

def read_users_and_locations_file(file_path: str = None) -> dict:
    return json.load(open(file_path))


class Queries(Enum):
    create_simple_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        location TEXT
    )
    '''

    add_user = 'INSERT INTO users (name, age, location) VALUES (%s, %s, %s)'
    query_all_users = "SELECT * FROM users"
    query_single_user = "SELECT * FROM users WHERE name = %s"
    query_single_user_by_age = "SELECT * FROM users WHERE age = %s"

class PsyDB:
    def __init__(self, **kwargs):
        self.db = kwargs.get('db')
        self.user = kwargs.get('user')
        self.pw = kwargs.get('pw')
        self.host = kwargs.get('host')
        self.port = kwargs.get('port')

        self.connection, self.cursor = None, None

    def __str__(self):
        return self.__dict__

    def __enter__(self):
        try:
            log.info(f'Connecting to {self.db} on {self.host}:{self.port}')

            self.connection = psycopg2.connect(
                database=self.db,
                user=self.user,
                password=self.pw,
                host=self.host,
                port=self.port
            )

            log.info('Connection succeeded.')

            return self
        except OperationalError as e:
            log.error(f'Connection failed:\n{e}')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        try:
            if self.connection:
                log.info('Closing database connection.')
                self.connection.close()
                return

            log.info('No connection to close.')

        except OperationalError as e:
            log.error(f'Unable to close connection.')

    def verify_connectivity(self):
        try:
            log.info('Verifying database connection.')

            if self.connection:
                if not self.connection.autocommit:
                    self.connection.autocommit = True

            if not self.cursor:
                self.cursor = self.connection.cursor()

        except OperationalError as e:
            log.error(f'Not connected to any database:\n{e}', exc_info=True)

    def execute_query(self, query):
        self.verify_connectivity()

        try:
            log.info(f'Executing: {query}')
            self.cursor.execute(query)

        except OperationalError as e:
            log.error(f'Query failed:\n{e}')

    def add_user(self, user_info: tuple = None) -> None:
        self.verify_connectivity()

        try:
            log.info(f'Writing new user to database: {user_info}')
            self.cursor.execute(Queries.add_user.value, user_info)

        except OperationalError as e:
            log.error(f'Unable to write to database:\n{e}', exc_info=True)

    def retrieve_data(self, query: str = None, query_params: tuple = None) -> list:
        self.verify_connectivity()

        try:
            if not query_params:
                log.info(f'Retrieving data for query: {query}')
                self.cursor.execute(query)

            else:
                log.info(f'Retrieving data for query: {query} | params: {query_params}')
                self.cursor.execute(query, query_params)

            return self.cursor.fetchall()

        except OperationalError as e:
            log.error(f'Unable to write to database:\n{e}', exc_info=True)


if __name__ == '__main__':
    # db_object = PsyDB(
    #     db='',
    #     user='',
    #     pw='',
    #     host='10.0.0.4',
    #     port=5432
    # )
    #
    # log.info(json.dumps(db_object.__str__(), indent=4))

    users_and_locations = read_users_and_locations_file('names_and_locations.json')

    # Generate 50 random users
    new_users = [(choice(users_and_locations['names']), randint(1, 80), choice(users_and_locations['locations']))
                 for x in range(50)]

    log.info('here')

    with PsyDB(
        db='dbtest',
        user='dbtest',
        pw='password',
        host='10.0.0.205',
        port=5432
    ) as pdb:
        pdb.execute_query(Queries.create_simple_table.value)

        # for user in new_users:
        #     pdb.add_user(user)

        current_users = pdb.retrieve_data(Queries.query_all_users.value)
        single_user = pdb.retrieve_data(Queries.query_single_user.value, ('gary',))
        by_age = pdb.retrieve_data(Queries.query_single_user_by_age.value, (37,))

    log.info(current_users)
    log.info(single_user)
    log.info(by_age)