#!/usr/bin/env python
if __name__ == '__main__':




    my_list = [10, 2, 3, 5, 12]
    total_1, total_2 = 0, 0

    print(my_list)

    for i in range(len(my_list)):
        total_1 += my_list[i]

    print(total_1)


    print(my_list)

    for i in my_list:
        total_2 += i

    print(total_2)

