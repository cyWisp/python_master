#!/usr/bin/env python
import os, sys

def print_directory_contents(s_path):
    for child in os.listdir(s_path):
        child_path = os.path.join(s_path, child)
        if os.path.isdir(child_path):
            print_directory_contents(child_path)
        else:
            print(child_path)

if __name__ == '__main__':

    file_path = sys.argv[1]

    print_directory_contents(file_path)
