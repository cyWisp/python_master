#!/usr/bin/env python
if __name__ == '__main__':

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    to_find = 5
    found = False

    for i in range(len(my_list)):
        found = my_list[i] == to_find
        if found:
            break

    if found:
        print(f"Element {to_find} found at index {i}")
    else:
        print("Element not found...")
