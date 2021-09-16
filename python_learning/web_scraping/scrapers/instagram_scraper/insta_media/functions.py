#!/usr/bin/env python
import os
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

def check_url(url):
    try:
        html = urlopen(url).read()
    except HTTPError as http_error:
        print(f"[x] HTTP Error encountered:\n{http_error}")
        exit(0)
    except URLError as url_error:
        print(f"[x] URL Error encountered:\n{url_error}")
        exit(0)
    else:
        return html

def check_path(path):
    if os.path.exists(path):
        print("[x] File Exists | [!] Exiting...")
        exit(0)
    else:
        return path

def check_args(arg_len, arg_list):
    if arg_len == 2 or arg_len == 4:
        if arg_len == 2:
            return check_url(arg_list[1]), "./"
        elif arg_len == 4:
            response = check_url(arg_list[1])
            if arg_list[2] == "-p":
                return response, arg_list[2]
            else:
                print(f"[!] Usage: {arg_list[0]} <URL> [-p <PATH>]")
                exit(0)
    else:
        print(f"[!] Usage: {arg_list[0]} <URL> [-p <PATH>]")
        exit(0)
        