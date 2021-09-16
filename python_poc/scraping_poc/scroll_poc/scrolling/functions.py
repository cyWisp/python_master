#!/usr/bin/env python
from sys import exit
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from parser import get_graph_image, get_graph_video, get_graph_sideCar

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

def usage(script_name):
    print(f"[!] Usage: {script_name} [-d, --dump] <URL> [-p, --path <PATH>]")
    print("[!] Options:")
    print("-d, --dump: Dump all profile media contents.")
    print("-p, --path: Specify output directory.")
    exit(0)

def check_args(arg_len, arg_list):

    if arg_len == 2 or arg_len == 4:
        if arg_len == 2:
            return check_url(arg_list[1]), ".", "single_post"
        elif arg_len == 4:
            if arg_list[2] == "-p" or arg_list[2] == "--path":
                return check_url(arg_list[1]), arg_list[3], "single_post"
            else:
                usage(arg_list[0])
    elif arg_len == 3 or arg_len == 5:
        if arg_len == 3:
            if arg_list[1] == "-d" or arg_list[1] == "--dump":
                return check_url(arg_list[2]), ".", "dump"
            else:
                usage(arg_list[0])
        elif arg_len == 5:
            if arg_list[3] == "-p" or arg_list[3] == "--path":
                return check_url(arg_list[2]), arg_list[4], "dump"
            else:
                usage(arg_list[0])    
    else:
        usage(arg_list[0])

def select_media(type_name, base_data, download_path):
    if type_name == 'GraphImage':
        get_graph_image(base_data, download_path)
    elif type_name == 'GraphVideo':
        get_graph_video(base_data, download_path)
    elif type_name == 'GraphSidecar' :
        get_graph_sideCar(base_data, download_path)
    else:
        print("[x] Media not found!")
        exit(0)

        