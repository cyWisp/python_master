#!/usr/bin/env python
from time import perf_counter
from random import randint

def bubble_sort(array):
    length = len(array)

    for i in range(length):
        already_sorted = True

        for j in range(length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array

def generate_array(max_l):
    start = perf_counter()
    print(f'Generating array.')

    arr = list()
    nums = [randint(1, max_l) for x in range(max_l)]

    for n in nums:
        if n not in arr:
            arr.append(n)

    end = perf_counter() - start
    print(f'Array length: {len(arr)} | Completed in {end:0.2f} seconds.')

    return arr

if __name__ == '__main__':

    max_limit = 100000
    test_arr = generate_array(max_limit)

    print(f'Running bubble sort on array containing {len(test_arr)} integers.')

    start = perf_counter()
    bubble_sort(test_arr)
    end = perf_counter() - start

    print(f'Completed in {end:0.2f} seconds.')


