#!/usr/bin/env python


if __name__ == '__main__':


    list_1 = [1, 2, 3]
    list_2 = ['a', 'b', 'c']

    zipped = zip(list_1, list_2)
    
    for z in zipped: print(z)
