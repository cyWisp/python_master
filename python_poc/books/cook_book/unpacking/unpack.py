#!/usr/bin/env python
import os, sys

# Any sequence (or iterable) can be unpacked into variables using a simple assignment operation. The only requirement
# is that the number of variables and structures match the sequence.

if __name__ == '__main__':

    items = ["Rob", "Alex", 54, ("love", "joy", "peace"), {"Mason": 1990, "Johnson": 2010},]

    name_1, name_2, num, emo_tuple, history_dict = items

    print("name_1:  {0}\nname_2: {1}\nnum: {2}\nemo_tuple: {3}\nhistory_dict: {4}".format(name_1, name_2, num, emo_tuple, history_dict))