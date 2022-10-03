#!/usr/bin/env python

def func(name, age, **kwargs):
    print(name)
    print(age)
    print(kwargs['location'])

if __name__ == '__main__':
    func('Rob', 12, location='Miami')

