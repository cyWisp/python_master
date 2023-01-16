#!/usr/bin/env python
import logging, decorators

@decorators.logging_deco
def add_nums(num_1, num_2):
    return num_1 + num_2

@decorators.logging_deco
def mult_nums(num_1, num_2):
    return num_1 * num_2

@decorators.logging_deco
def get_array():
    return [i for i in range(5)]

if __name__ == '__main__':
    decorators.configure_logging()

    add_nums(1, 2)
    mult_nums(2, 3)
    get_array()

