#!/usr/bin/env python

def csv_reader(file_name: str):
    for row in open(file_name, 'r'):
        yield row

if __name__ == '__main__':
    csv_content = csv_reader('sample.csv')

    for i in csv_content:
        print(i)