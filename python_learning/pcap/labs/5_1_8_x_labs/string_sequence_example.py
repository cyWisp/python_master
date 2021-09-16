#!/usr/bin/env python
if __name__ == '__main__':

    str_1 = "Robert Daglio"

    for c in range(len(str_1)):
        print(f"{str_1[c]}", end=" ")
    print()

    for c in str_1:
        print(c, end=" ")
    print()
