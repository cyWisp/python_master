#!/usr/bin/env python

var_str = "This is a coding test, I like coding because it is fun"


if __name__ == '__main__':
    var_dict = {index: i for index, i in enumerate(var_str.split(' '))}
    reversed_list = list()
    counter = int(list(var_dict.keys())[-1])

    for i in range(len(var_dict)):
        if var_dict[counter] not in reversed_list:
            reversed_list.append(var_dict[counter])
        counter -= 1

    print(' '.join(reversed_list))
