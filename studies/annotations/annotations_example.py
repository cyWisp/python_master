#!/usr/bin/env python


def return_two() -> tuple[str, str]:
    return 'hi', 'there'


if __name__ == '__main__':
    tuple_var = return_two()
    var_one, var_two = return_two()

    print(f'tuple var: {tuple_var} | type: {type(tuple_var)}')
    print(f'var one: {var_one} | type: {type(var_one)}')
    print(f'var two: {var_two} | type: {type(var_two)}')