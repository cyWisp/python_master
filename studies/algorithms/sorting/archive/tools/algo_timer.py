#!/usr/bin/env python
from time import perf_counter
from random import randint

import configargparse
import logging
import json

parser = configargparse.get_argument_parser(
    name='default',
    description='parameters for running bubble sort',
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter
)

parser.add_argument('--log-level', '-lL', type=str, required=False,
                    default='INFO', help='Log level specification.')

parser.add_argument('--array-length', '-aL', type=int, required=False,
                    default=20, help='The length of the array to process')

parser.add_argument('--iterations', '-i', type=int, required=False,
                    default=3, help='The number of times to run the algorithm.')

parser.add_argument('--algorithm', '-a', type=str, required=False,
                    default='bubble', help='The algorithm to run: ["bubble"]')

cfg = parser.parse_known_args()[0]

logging.basicConfig(
    format='%(asctime)s - %(levelname)s: %(message)s',
    level=logging.getLevelName(cfg.log_level.upper())
)
log = logging.getLogger()


def bubble_sort(array: list) -> list:
    log.debug(f'Starting {bubble_sort.__name__}.')
    length = len(array)

    for i in range(length):
        log.debug(f'Pass {i + 1}: {array}')

        already_sorted = True

        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array

def generate_array(length: int):
    log.debug(f'Generating array of {length} numbers.')

    new_arr = list()
    while len(new_arr) != length:
        random_number = randint(1, length)
        if random_number not in new_arr:
            new_arr.append(random_number)

    log.debug(f'New array: {str(new_arr)}')
    return new_arr


ALGORITHMS = {
    'bubble': bubble_sort
}


def run_algorithm(algo: str, iterations: int):
    log.info(f'Algorithm: {algo} | Array length: {cfg.array_length} | Iterations: {iterations}')

    run_times = list()
    result = None

    for i in range(iterations):
        array = generate_array(cfg.array_length)

        start = perf_counter()
        result = ALGORITHMS[algo](array)
        end = perf_counter() - start

        run_times.append(f'{end:0.7f}')

        log.debug(f'Sorted: {result}')

    return run_times


def get_stats(run_times: list):
    log.info(f'All times: {json.dumps(run_times, indent=4)}')
    log.info(f'Minimum execution time: {min(run_times)}s')
    log.debug(f'Maximum execution time: {max(run_times)}s')
    log.debug(f'Average execution time: {(sum([float(x) for x in run_times]) / float(len(run_times))):0.7f}s')


if __name__ == '__main__':
    log.debug(json.dumps(vars(cfg), indent=4))
    times = run_algorithm(cfg.algorithm, cfg.iterations)
    get_stats(times)