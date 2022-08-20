#!/usr/bin/env python
import logging
import json
import configargparse
from random import randint
from timeit import repeat


parser = configargparse.get_argument_parser(
    name='default',
    description='Default arguments for timer.py'
)

parser.add_argument('--array-length', '-a', type=int, default=20, help='Length of array to process')
parser.add_argument('--iterations', '-i', type=int, default=10, help='Iterations- number of times to run algorithm')
parser.add_argument('--algorithm', '-aL', type=str, default='bubble_sort', help='The algorithm to test.')

cfg = parser.parse_known_args()[0]


logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


def run_sorting_algorithm(algorithm: str, array: list, iters: int):
    """
    Set up the context and prepare the call to the specified
    algorithm using the supplied array. Only import the
    algorithm function if it's not the built-in `sorted()`.

    :param algorithm: str
    :param array: list
    :param iters: int
    :return: None
    """

    setup_code = f'from __main__ import {algorithm}' if algorithm != 'sorted' else ''
    stmt = f'{algorithm}({array})'

    # Execute the code ten different times and return the elapsed time
    # for each execution.

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=iters)

    # Finally, display the name of the algorithm and the
    # minumum time it took to run

    log.info(f'Algorithm: {algorithm}. Minimum execution time: {min(times):0.2f}')

if __name__ == '__main__':

    log.info(json.dumps(vars(cfg), indent=4))


    # Generate an array of x length items consisting
    # of random integer values between 0 and 999

    # arr = [randint(0, 1000) for x in range(1000000)]

    # Call the function using the name of the sorting algorithms
    # and the array you just created

    # run_sorting_algorithm(algorithm='sorted', array=arr)

    from bubble.bubble import bubble_sort

    arr = [randint(1, cfg.array_length) for x in range(cfg.array_length)]
    run_sorting_algorithm(algorithm='bubble_sort', array=arr, iters=cfg.iterations)