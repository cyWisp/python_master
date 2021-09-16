#!/usr/bin/env python
if __name__ == '__main__':

    my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
    new_list = []

    for i in range(len(my_list)):
        if my_list[i] in my_list[i+1:]:
            pass
        else:
            new_list.append(my_list[i])
    
    print(my_list)
    print(new_list)





