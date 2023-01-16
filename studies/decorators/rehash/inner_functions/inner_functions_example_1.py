#!/usr/bin/env python

def parents():
    print('Printing from the parent() function')

    def first_child():
        print('Printing from the first_child() function.')

    def second_child():
        print('Printing from the second_child() function.')

    second_child()
    first_child()


if __name__ == '__main__':
    parents()