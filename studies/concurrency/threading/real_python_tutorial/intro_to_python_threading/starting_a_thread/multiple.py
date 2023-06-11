#!/usr/bin/env python
import logging
import threading
import time
import uuid

logging.basicConfig(
    datefmt='%Y-%m-%d %H:%M:%S',
    format='%(process)d - %(filename)s - %(funcName)s - %(asctime)s: %(message)s',
    handlers=[logging.StreamHandler()],
    level=logging.INFO
)

log = logging.getLogger()


def greet(name: str, id: str):
    log.info(f'Starting thread {id}.')
    time.sleep(2)

    log.info(f'Hello {name}.')
    time.sleep(1)

    log.info(f'Thread {id} finished.')


if __name__ == '__main__':
    log.info('Starting MAIN.')

    names = [
        'Rob',
        'Allan',
        'Mike',
        'Tiffany',
        'Steve',
        'Alex'
    ]

    greet_threads = list()

    for name in names:
        new_thread = threading.Thread(target=greet, args=(name, uuid.uuid4()))
        greet_threads.append(new_thread)
        new_thread.start()

    for thread in greet_threads:
        thread.join()

    log.info('All threads terminated.')
