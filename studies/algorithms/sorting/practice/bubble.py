#!/usr/bin/env python
from random import randint


def generate_array(length: int = 0) -> list:
    new_array = list()

    if length:
        while len(new_array) != length:
            random_number = randint(1, length)
            if random_number not in new_array:
                new_array.append(random_number)

        return new_array
    else:
        print('Please provide a positive integer.')


def bubble_sort(array: list) -> list:
    n = len(array)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break
    return array

if __name__ == '__main__':
    array = generate_array(20)
    print(array)

    sorted_array = bubble_sort(array)
    print(sorted_array)