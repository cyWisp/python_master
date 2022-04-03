#!/usr/bin/env python
import os

if __name__ == '__main__':

    dog_names = ['fido', 'ralph', 'pupper', 'johnny']
    to_append = ['bamBam', 'simon']

    for name in to_append:
        dog_names.append(name)

    for name in dog_names:
        print(name)
