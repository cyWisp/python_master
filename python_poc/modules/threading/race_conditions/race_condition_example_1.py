#!/usr/bin/env python
import time, logging, threading
import concurrent.futures

class Fake_Database():
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info(f"Thread {name}    : starting update...")
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info(f"Thread {name}    : finishing update...")

if __name__ == '__main__':

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    database = Fake_Database()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)

    logging.info(f"Testing update. Ending value is {database.value}")
