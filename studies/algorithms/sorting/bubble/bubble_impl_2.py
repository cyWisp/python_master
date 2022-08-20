#!/usr/bin/env python
from random import randint
from timeit import repeat

def run_algo(algo, array, iters):
    setup_code = f'from __main__ import {algo}' if algo != 'sorted' else ''
    stmt = f'{algo}({array})'

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=iters)

    print(f'Algorithm: {algo}\nMinimum execution time: {min(times)}')
    print(f'Array length: {len(array)}\nIterations: {iters}')

def bubble_sort(array):
    n = len(array)
    print(f'Array length: {n}')

    for i in range(n):
        print(f'Pass: {i} ', end='')
        print(array)

        already_sorted = True

        limit = n - i - 1
        print(f'Current limit: {limit}')

        for j in range(limit):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array

if __name__ == '__main__':
    max = 100000

    nums = [randint(1, max) for x in range(1, max)]
    arr = list()

    for num in nums:
        if num not in arr:
            arr.append(num)

    run_algo(algo='bubble_sort', array=arr, iters=10)
