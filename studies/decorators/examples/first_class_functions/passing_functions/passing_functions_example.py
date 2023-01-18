#!/usr/bin/env python

def say_hi(some_string):
    return f"Hi {some_string}"


def func_1(text, some_func):
    return some_func(text)


if __name__ == '__main__':
    print(func_1('Bob', say_hi))

