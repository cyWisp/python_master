import logging
import sys
import json
import mysql.connector
from mysql.connector import Error, InterfaceError


log = logging.getLogger()
log.setLevel(logging.INFO)


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
        self.connection_error = False

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
                log.debug(f'{type(result)} | {result}')
                return result

            else:
                log.debug('Query executed successfully.')
                return []   # return empty list

        except Error as e:
            log.error(f'Failed to execute query: {e}')

    def verify_cursor(self):
        try:
            if not self.cursor:
                self.cursor = self.connection.cursor()

        except Error as e:
            log.error(f'Cursor creation failed:\n{e}')
            sys.exit()

    def verify_connection(self):
        if not self.connection_error:
            if not self.connection:
                self.connect()
        else:
            sys.exit(1)

    def disconnect(self):
        try:
            if self.connection:
                self.connection.disconnect()
                log.debug('Disconnected from database.')

        except Error as e:
            log.error(f'Disconnection process failed.\n{e}', exc_info=True)

    def connect(self):
        retry_count = 1

        if not self.connection:
            while True:
                try:
                    if retry_count == self.MAX_CONNECTION_RETRIES:
                        raise TimeoutError('Max retry count exceeded.')

                    log.debug(f'Connecting to {self.host}:{self.port} | Attempt: {retry_count}')

                    self.connection = mysql.connector.connect(
                        host=self.host,
                        port=self.port,
                        user=self.username,
                        passwd=self.password,
                        database=self.db_name
                    )

                    log.debug('Connection succeeded!')
                    break

                except (Error, InterfaceError) as e:
                    log.error(f'Connection failed:\n{e}\nRetrying...')
                    retry_count += 1

                except TimeoutError as e:
                    log.error(f'{e} Terminating operation.')
                    self.connection_error = True
                    break


if __name__ == '__main__':

    with MSInterface(
        'ap',
        'localhost',
        'root',
        'password'
    ) as mi:
        log.info(mi.__str__())
        db_description = mi.execute_query('DESCRIBE invoices;')
        ten_invoices = mi.execute_query('SELECT * FROM invoices LIMIT 0, 10;')

        log.info(json.dumps(db_description, indent=4))
        log.info(json.dumps(ten_invoices, indent=4))

