#!/usr/bin/env python
from sys import argv, exit
from functions import check_args
from parser import parse_data, get_graph_image

if __name__ == '__main__':
    html, path = check_args(len(argv), argv)
    base_data, type_name = parse_data(html)
    get_graph_image(base_data, path)

    

    #print(f"path: {path}\nhtml: \n\n{html}")
