#!/usr/bin/env python
import random
import time
import logging
import functools

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

time_lapsed = list()


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.perf_counter()
        r_nums = func(*args, **kwargs)

        time_lapsed.append(f'{(time.perf_counter() - start)}')
        return r_nums
    return wrapper_timer


@timer
def rng(num_range: int = 20):
    return [random.randint(1, num_range) for _ in range(num_range)]


if __name__ == '__main__':
    random_nums = rng(1000)
    log.info(f'Time lapsed: {time_lapsed[0]}')

    log.info(f'Nums: {random_nums}')

