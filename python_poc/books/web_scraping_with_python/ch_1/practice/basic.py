#!/usr/bin/env python
from urllib.request import urlopen

if __name__ == '__main__':
    
    html = (urlopen(input("Url: "))).read()
    print(html)
    