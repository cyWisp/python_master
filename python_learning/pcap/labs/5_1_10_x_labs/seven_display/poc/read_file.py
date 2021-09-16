#!/usr/bin/env python

if __name__ == '__main__':

    with open("file.txt", 'r+') as read_file:
        contents = [x for x in read_file]
    read_file.close()

    print(contents)
