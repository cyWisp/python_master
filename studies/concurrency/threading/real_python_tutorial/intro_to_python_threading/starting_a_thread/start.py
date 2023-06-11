#!/usr/bin/env python

import logging
import threading
import time

from uuid import uuid4

logging.basicConfig(
    datefmt='%Y-%m-%d %H:%M:%S',
    format='%(process)d - %(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s',
    handlers=[logging.StreamHandler()],
    level=logging.INFO
)

log = logging.getLogger()


def thread_function(name):
    log.info(f'Thread: {name}: starting.')
    time.sleep(2)
    log.info(f'Thread: {name}: finishing.')


if __name__ == '__main__':
    log.info('Starting MAIN.')

    new_thread = threading.Thread(target=thread_function, args=(uuid4(),))
    new_thread.start()

    log.info('MAIN: waiting for thread to terminate.')
    new_thread.join()

    log.info('MAIN: done.')
