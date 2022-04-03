#!/usr/bin/env python
import os
from sys import exit, argv
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def check_args():
    if len(argv) is not 2:
        print(f"[!] Usage: {argv[0]} <URL>")
        exit()
    else:
        return argv[1]

def get_html(url):
    try:
        raw = urlopen(url).read()
    except HTTPError as http_error:
        print(f"[x] Something went wrong! | {http_error}")
    except URLError as url_error:
        print(f"[x] Something went wrong! | {url_error}")
    else:
        return raw

def return_format(raw):
    return BeautifulSoup(raw, 'html.parser').prettify()

def get_links(raw):
    a_tags = BeautifulSoup(raw, 'html.parser').findAll('a')
    links = [x['href'] for x in a_tags]
    clickable = [argv[1] + l.lstrip('.') for l in links]
    return clickable

def read_links(links):
    sources = [return_format(get_html(l)) for l in links]
    pages = [l.split('/')[-1] for l in links]
    indices = dict(zip(pages, sources))
    return indices

#    for i, p in indices.items():
#        print(f"{i}:\n{p}\n==========================================================\n")

def write_site(site_files):
    for p, s in site_files.items():
        try:
            with open(f'./{p}', 'w+') as new_file:
                new_file.write(s)
        except:
            print('[x] Write failed...')
            continue
        else:
            print(f"[!] Writing {p}...")
        finally:
            new_file.close()
    print("[*] Done!")

if __name__ == '__main__':
    
    url = check_args()
    html = get_html(url)
    links = get_links(html)
    page_dict = read_links(links)
    write_site(page_dict)

    
    


