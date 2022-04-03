#!/usr/bin/env python

def diff(list_1, list_2):
    return (list(set(list_1) - set(list_2)))

if __name__ == '__main__':

    names_1 = ["rob", "taz", "ben", "tom", "robin", "chaz"]
    names_2 = ["rob", "taz", "ben", "bill", "john", "higgins"]

    print(f"list 1: {names_1}\nlist_2: {names_2}")
    print(f"Diff: {diff(names_1, names_2)}")
