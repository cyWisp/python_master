#!/usr/bin/env python
import logging
import time

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


class SimpleExample:
    def __init__(self, input_size: int):
        self.input_size = input_size

    def __str__(self):
        return vars(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def append_then_reverse(self):
        nums = []

        for i in range(self.input_size):
            nums.append(i)

        nums.reverse()

    def append_while_reverse(self):
        nums = []

        for i in range(self.input_size):
            nums.insert(0, i)


if __name__ == '__main__':
    start, end = None, None

    with SimpleExample(10**5) as se:
        start = time.perf_counter()

        se.append_while_reverse()

        end = time.perf_counter() - start

    log.info(f'Execution time: {end}')