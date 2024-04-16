#!/usr/bin/env python
import random
import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('app.log', 'w+', encoding='utf-8')
    ]
)
log = logging.getLogger()


def generate_array(number_range: tuple, quantity: int) -> list:
    try:
        log.info(f'Generating an array of {quantity} integers.\n'
                 f'Min: {number_range[0]} | Max: {number_range[1]}')

        original_array = [random.randint(number_range[0], number_range[1]) for _ in range(quantity)]
        log.info(f'Original array: {original_array}')

        return original_array
    except Exception as e:
        log.exception(e)


# def bubble_sort(arr: list) -> list:
#     arr_length = len(arr)
#     log.info(f'arr_length: {arr_length}')
#
#     for i in range(arr_length):
#         already_sorted = True
#
#         for j in range(arr_length - i - 1):
#             log.info(f'Outer loop iter: {i}')
#             log.info(f'Inner loop iter: {j} | {arr_length} - {i} - 1 = {arr_length - i - 1}')
#             log.info(f'Array state: {arr}\n')
#
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 already_sorted = False
#
#         if already_sorted:
#             break


def bubble_sort(arr: list) -> list:
    # Determine the length of the array
    array_length = len(arr)

    # Iterate through the array
    for i in range(array_length):
        # Create a sentinel to check whether or not
        # the array is already sorted
        already_sorted = True

        for j in range(array_length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False

        if already_sorted:
            break

    return arr



if __name__ == '__main__':
    nums = generate_array((1, 99), 10)
    sorted_array = bubble_sort(nums)

    log.info(f'Sorted array: {sorted_array}')
