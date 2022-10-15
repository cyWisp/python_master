#!/usr/bin/env python
from random import randint
import logging

logging.basicConfig(
    format='%(levelname)s: %(message)s',
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()]
)
log = logging.getLogger()


def generate_array(length: int) -> list:
    arr = list()

    while len(arr) != length:
        random_number = randint(1, length)
        if random_number not in arr:
            arr.append(random_number)

    return arr


def insertion_sort(array: list) -> list:
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array

if __name__ == '__main__':
    nums = generate_array(20)
    log.debug(f'Original array: {nums}')

    sorted_arr = insertion_sort(nums)
    log.debug(f'Sorted array: {sorted_arr}')