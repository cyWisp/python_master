#!/usr/bin/env python
import logging
import uuid

from uuid import uuid4
from multiprocessing import Pool
from time import time

logging.basicConfig(
    level=logging.INFO,
    format='%(process)d - %(filename)s - %(funcName)s - %(levelname)s: %(message)s'
)
log = logging.getLogger()

COUNT = 5000000


def countdown(n, process_name: str) -> str:
    log.info(f'Starting process: {process_name}')
    while n > 0:
        n -= 1

    return process_name


def normal_func(process_name):
    log.info(f'Starting process {process_name}')
    log.info([x for x in range(10)])


if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time()

    normal_func(str(uuid.uuid4()))

    r1 = pool.apply_async(countdown, [COUNT // 2, str(uuid.uuid4())])
    r2 = pool.apply_async(countdown, [COUNT // 2, str(uuid.uuid4())])

    pool.close()
    pool.join()

    end = time()

    normal_func(str(uuid.uuid4()))

    log.info(f'Time lapsed: {end - start}')
    log.info(f'R1 return value: {r1.get()}')
    log.info(f'R2 return value: {r2.get()}')


