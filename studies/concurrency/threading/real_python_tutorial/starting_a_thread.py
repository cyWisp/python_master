#!/usr/bin/env python
import logging
import threading
import time
from analytics.decorators import timer
from random import choice

color = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)

logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.INFO
)

log = logging.getLogger()


def thread_function(name):
    log.info(f'Thread {choice(color[1:])} {name} {color[0]} starting.')
    time.sleep(2)
    log.info(f'Thread {name} finishing.')


if __name__ == '__main__':

    num_threads = 10

    log.info(f'Building {num_threads} threads.')
    threads = [threading.Thread(target=thread_function, args=(x + 1, )) for x in range(num_threads)]

    log.info('Main - Preparing to initialize threads.')

    for t in threads:
        log.info(f'Initializing thread {t}.')
        t.start()

    for t in threads:
        t.join()

    log.info('All threads finished.')
