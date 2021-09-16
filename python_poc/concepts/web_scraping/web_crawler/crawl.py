#!/usr/bin/env python
from lxml import html
import requests
import sys

# Base url from where the crawl begins
base  = sys.argv[1]

#Function to get the links and their status
def getlinks(url):
    response = requests.get(url)
    if (response.status_code == 200):
        status = '[OK]'
    else:
        status = '[BROKEN]'
    print(status, url )
    pagehtml = html.fromstring(response.content)
    page_links = pagehtml.xpath("//a[not(@rel='nofollow') and not(contains(@href,'#'))]/@href")
    return page_links

site_links =[base]

#Repeat for each link discovered
for item in site_links:
    #absolute link
    if item.startswith('http://') or item.startswith('https://'):
        url = item
    #root-relative link
    elif item.startswith('/'):
        url = base + item
    else:
        url=base + "/" + item
    
    page_links = getlinks(url)
    for link in page_links:
        if link not in site_links:
                site_links.append(link)
