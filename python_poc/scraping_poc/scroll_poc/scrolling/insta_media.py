#!/usr/bin/env python
import os, time
from sys import argv
from functions import check_args, select_media
from parser import parse_data, load_js, dump
from urllib.request import urlopen
from splash import show_splash

if __name__ == '__main__':

    os.system('clear')
    show_splash()
    time.sleep(1)
    
    # Parse all given arguments and return needed values
    html, path, op_type = check_args(len(argv), argv)
    
    # Process link as a single post url
    if op_type == "single_post":
        base_data, type_name = parse_data(html)
        select_media(type_name, base_data, path)
        print("[*] Done!")
    # Process comprehensive dump of all media
    else:
        # 
        # Use selenium to preload embedded js
        html = load_js(argv[2])   

        links, dump_dir = dump(html, argv[2], path)
        for l in links:
            link_html = urlopen(l).read()
            base_data, type_name = parse_data(link_html)
            select_media(type_name, base_data, dump_dir)
        print("[*] Done!")

