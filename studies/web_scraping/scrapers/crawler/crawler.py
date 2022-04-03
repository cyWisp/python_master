#!/usr/bin/env python
from sys import argv
from functions import check
from scraper import Scraper

if __name__ == '__main__':

    check(len(argv), argv[0])
    scraper_object = Scraper(argv[1])

    links = scraper_object.find_page_links()
    parsed = scraper_object.print_formatted()

    [print(l) for l in links]
    print('\n')
    print(parsed)

    
    





