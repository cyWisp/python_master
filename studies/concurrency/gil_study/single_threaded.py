#!/usr/bin/env python
import time
import logging
from threading import Thread

logging.basicConfig(level=logging.INFO)
COUNT = 5000000


def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    start = time.time()
    countdown(COUNT)

    end = time.time()

    logging.info(f'Time taken in seconds: {end - start}')