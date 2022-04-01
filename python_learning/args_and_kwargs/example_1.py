#!/usr/bin/env python

def some_func(script_name=__name__, **kwargs):
    print(script_name)

    for k, v in kwargs.items():
        print(f'{k}: {v}')

def some_other_func(*args):
    for a in args:
        print(a)

if __name__ == '__main__':
    arg_dict = {
        'name': 'Rob',
        'age': 36,
        'location': 'Miami'
    }

    arg_list = [
        'first item',
        'second item',
        'third item'
    ]

    some_func(**arg_dict)
    some_other_func(*arg_list)
