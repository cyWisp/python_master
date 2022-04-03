#!/usr/bin/env python
if __name__ == '__main__':

    names = ['rob', 'tom', 'al', 'marco']

    print(f"current list: {names}")

    print("inserting 'jim' as the second element...")
    names.insert(1, "jim")

    print(f"new list: {names}")

    print("inserting 'mellow' as the third element...")
    names.insert(2, 'mellow')

    print(f"new list: {names}")
