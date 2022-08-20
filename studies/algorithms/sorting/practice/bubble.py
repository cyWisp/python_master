#!/usr/bin/env python
from random import randint

def bubble_sort(array):
    length = len(array)

    for i in range(length):
        already_sorted = True
        for j in range(length - i - 1):
            print(f'Pass {i}: {array}')
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break
    return array

def generate_array(length: int):
    arr = list()

    while len(arr) != length:
        random_number = randint(1, length)
        if random_number not in arr:
            arr.append(random_number)
    return arr

if __name__ == '__main__':
    arr = generate_array(20)

    sorted_array = bubble_sort(arr)