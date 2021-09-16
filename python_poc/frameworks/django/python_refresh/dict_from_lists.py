#!/usr/bin/env python
import os

if __name__ == '__main__':

    list_1 = ['first', 'second', 'third', 'fourth']
    list_2 = ['f_1', 'f_2', 'f_3', 'f_4']

    new_dict = {}

    for x in range(0, len(list_1)):
        new_dict[list_1[x]] = list_2[x]

    for key, value in new_dict.items():
        print('{0}: {1}'.format(key, value))
