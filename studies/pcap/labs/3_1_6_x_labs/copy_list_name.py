#!/usr/bin/env python

if __name__ == '__main__':

    # Proving that copying a list does not copy its contents,
    # But rather creates another pointer that ultimately points
    # To the same location in memory

    list_1 = ['Rob', 'sam', 'tommy']
    print(f"list_1: {list_1}")

    list_2 = list_1

    print(f"list_2: {list_2}")

    list_1.remove('Rob')

    print(f"list_2: {list_2}")

