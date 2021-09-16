from bs4 import BeautifulSoup
from urllib.request import urlopen, Request, urlretrieve
import requests, re, json
import os, sys, argparse

def get_soup(url, header):
    
    return BeautifulSoup(urlopen(Request(url, headers=header)), 'lxml')

def get_args():

    parser = argparse.ArgumentParser(description='Google Image Scraper')
    parser.add_argument('-s', '--search', default='banana hammock', type=str, help='Search Criteria...')
    parser.add_argument('-n', '--num_images', default=10, type=int, help='Number of Images...')
    parser.add_argument('-d', '--directory', default='./pictures', type=str, help='Destination Directory')
    args = parser.parse_args()

    query = args.search
    max_images = args.num_images
    save_directory = args.directory

    return query, max_images, save_directory

if __name__ == '__main__':

    search_crit, number_of_images, target_dir = get_args()

    search_crit = search_crit.split()
    search_crit = '+'.join(search_crit)

    url = "https://www.google.co.in/search?q="+search_crit+"&source=lnms&tbm=isch"
    header = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup_object = get_soup(url, header)
    
    images = []

    for item in soup_object.find_all("div",{"class":"rg_meta"}):
        link, Type = json.loads(item.text)["ou"], json.loads(item.text)["ity"]
        images.append((link, Type))

    for item, (img, Type) in enumerate(images[0:number_of_images]):
        try:
            if len(Type) == 0:
                urlretrieve(img, os.path.join(target_dir, "img_{0}.jpg".format(str(item))))
            else:
                urlretrieve(img, os.path.join(target_dir, "img_{0}.{1}".format(str(item),Type)))
        except:
            print("[x] Something went wrong...\n[x] Could not load {0}".format(img))
