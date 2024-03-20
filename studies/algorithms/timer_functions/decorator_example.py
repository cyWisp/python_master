import logging
import time
import functools
import random
import json

from datetime import datetime
from uuid import uuid4

logging.basicConfig(level=logging.INFO, format='%(message)s')
log = logging.getLogger()


results = []


# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time.perf_counter()
#         result = func(*args, **kwargs)
#         results.append(time.perf_counter() - start)
#
#         if result:
#             return result
#
#     return wrapper


class Timer:
    def __init__(self):
        self.results = {}

    def append_result(
        self,
        func_name: str,
        start_time: str,
        elapsed: str
    ):
        self.results[f'{func_name} - {start_time} {str(uuid4())}'] = elapsed

    def perf_counter_timer(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start, start_time = time.perf_counter(), datetime.strftime(datetime.now(), '%y-%m-%d %H:%M:%S')
            result = func(*args, **kwargs)
            self.append_result(func.__name__, start_time, str(time.perf_counter() - start))

            if result:
                return result

        return wrapper


new_timer = Timer()


@new_timer.perf_counter_timer
def generate_nums(qty: int, lower_limit: int, upper_limit: int) -> list:
    return [random.randint(lower_limit, upper_limit) for _ in range(qty)]


if __name__ == '__main__':

    for i in range(5):
        random_numbers = generate_nums(10000, 1, 999)

    log.info(json.dumps(new_timer.results, indent=4))