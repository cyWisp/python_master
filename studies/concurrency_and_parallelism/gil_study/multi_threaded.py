#!/usr/bin/env python
import time, logging
from threading import Thread

COUNT = 5000000
logging.basicConfig(level=logging.INFO)

def countdown(n):
    while n > 0:
        n -= 1


if __name__ == '__main__':
    t1 = Thread(target=countdown, args=(COUNT//2,))
    t2 = Thread(target=countdown, args=(COUNT // 2,))

    start = time.time()

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    end = time.time()

    logging.info(f'Time taken in seconds: {end - start}')
