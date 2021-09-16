#!/usr/bin/env python
import logging, threading, concurrent.futures, time

logging.basicConfig(
    format="%(process)d - %(asctime)s: %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)

class FakeDataBase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def locked_update(self, name):
        logging.info(f"Thread {name} starting update...")
        logging.debug(f"Thread {name} about to lock...")

        with self._lock:
            logging.debug(f"Thread {name} has lock...")
            local_copy = self.value
            local_copy += 1

            time.sleep(0.1)

            self.value = local_copy
            logging.debug(f"Thread {name} about to release lock...")
        logging.debug(f"Thread {name} after release...")
        logging.info(f"Thread {name} finishing update...")

if __name__ == '__main__':

    logging.getLogger().setLevel(logging.DEBUG)

    db = FakeDataBase()
    logging.info(f"Testing update. Starting value is {db.value}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(db.locked_update, index)

    logging.info(f"Testing update. Ending value is: {db.value}")

