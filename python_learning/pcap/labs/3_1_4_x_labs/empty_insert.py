#!/usr/bin/env python
if __name__ == '__main__':

    my_list_1, my_list_2 = list(), list()
    

    for i in range(5):
        my_list_1.append(i + 1)

    print(my_list_1)

    for i in range(5):
        my_list_2.insert(0, i + 1)

    print(my_list_2)
