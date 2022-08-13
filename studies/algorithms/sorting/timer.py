#!/usr/bin/env python
import logging
from random import randint
from timeit import repeat

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


def run_sorting_algorithm(algorithm, array: list):
    """
    Set up the context and prepare the call to the specified
    algorithm using the supplied array. Only import the
    algorithm function if it's not the built-in `sorted()`.

    :param algorithm:
    :param array:
    :return:
    """

    setup_code = f'from __main__ import {algorithm}' if algorithm != 'sorted' else ''
    stmt = f'{algorithm}({array})'

    # Execute the code ten different times and return the elapsed time
    # for each execution.

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minumum time it took to run

    log.info(f'Algorithm: {algorithm}. Minimum execution time: {min(times)}')

if __name__ == '__main__':
    # Generate an array of x length items consisting
    # of random integer values between 0 and 999

    arr = [randint(0, 1000) for x in range(1000000)]

    # Call the function using the name of the sorting algorithms
    # and the array you just created

    run_sorting_algorithm(algorithm='sorted', array=arr)