#!/usr/bin/env python
from sys import exit
if __name__ == '__main__':

    # this demonstrates the usage of the in and not in operators

    names = ['Rob', 'John', 'Tom', 'Ben', 'Anthony']

    while True:
        user_input = input('Name: ')
        for name in names:
            if user_input in names:
                print(f"Element {user_input} is present!")
                break
            elif user_input == 'exit':
                print('Good bye!')
                exit(0)
            else:
                print(f"Element {user_input} is not present. Try again!")
                break
