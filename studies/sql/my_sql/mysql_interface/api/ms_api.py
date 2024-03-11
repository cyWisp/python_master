import logging
import json
import mysql.connector
from mysql.connector import Error

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


class MSInterface:
    MAX_CONNECTION_RETRIES = 5

    def __init__(
        self,
        db_name: str,
        host: str,
        username: str,
        password: str,
        port: int = 3306,
        instance: str = None
    ):
        self.db_name, self.host, self.port = db_name, host, port
        self.username, self.password = username, password

        self.connection, self.instance = None, instance
        self.cursor = None

        self.connect()

    def __str__(self):
        return vars(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_value, exc_type, exc_traceback):
        self.disconnect()

    def execute_query(self, query: str) -> list:
        self.verify_connection()
        self.verify_cursor()

        try:
            self.cursor.execute(query)
            result = [tuple([str(x) for x in y]) for y in self.cursor.fetchall()]

            log.info(f'{query} ->')

            if result:
                log.info(f'{type(result)} | {result}')
                return result

            else:
                return []   # return empty list

        except Error as e:
            log.error(f'Failed to execute query: {e}')

    def verify_cursor(self):
        try:
            if not self.cursor:
                self.cursor = self.connection.cursor()

        except Error as e:
            log.error(f'Cursor creation failed:\n{e}')

    def verify_connection(self):
        if not self.connection:
            self.connect()

    def disconnect(self):
        try:
            if self.connection:
                self.connection.disconnect()
                log.info('Disconnected from database.')

        except Error as e:
            log.error(f'Disconnection process failed.\n{e}', exc_info=True)

    def connect(self):
        retry_count = 1

        if not self.connection:
            while True:
                try:
                    if retry_count == self.MAX_CONNECTION_RETRIES:
                        raise TimeoutError('Max retry count exceeded.')

                    log.info(f'Connecting to {self.host}:{self.port} | Attempt: {retry_count}')

                    self.connection = mysql.connector.connect(
                        host=self.host,
                        port=self.port,
                        user=self.username,
                        passwd=self.password,
                        database=self.db_name
                    )

                    log.info('Connection succeeded!')
                    break

                except (Error, mysql.connector.InterfaceError, TimeoutError) as e:
                    log.error(f'Connection failed:\n{e}', exc_info=True)
                    retry_count += 1


if __name__ == '__main__':

    with MSInterface(
        'ap',
        'localhost',
        'root',
        'password'
    ) as mi:
        log.info(mi.__str__())
        desc = mi.execute_query('DESCRIBE invoices;')
        desc = mi.execute_query('SELECT * FROM invoices;')
        log.info(type(desc))


