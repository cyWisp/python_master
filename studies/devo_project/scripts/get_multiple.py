#!/usr/bin/env python
#!/usr/bin/env python
import requests, logging
from calendar import month_name
from bs4 import BeautifulSoup
from os import system
from time import sleep
from datetime import datetime

F2F = 'https://www.kcm.org/read/faith-to-faith'
TODAY = str(datetime.today()).split(" ")[0]
DAY = TODAY.split("-")[2]
MONTH = int(TODAY.split("-")[1])
YEAR = TODAY.split("-")[0]
DATE = f"{DAY} {month_name[MONTH]} {YEAR}"

def configure_logging():
    format = "%(process)d - %(asctime)s: %(message)s"
    logging.basicConfig(
        format = format,
        datefmt = "%H:%M:%S",
        level = logging.INFO,
        handlers = [logging.FileHandler('./app.log', 'w', 'utf-8')]
    )

def logger(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        logging.info(value)
        return value
    return wrapper

def get_html(url):
    return requests.get(url).text

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    p = soup.findAll('p')
    return p

def strip_content(p):
    pars = [i.text for i in p if "Victory" not in i.text and "Kenneth" not in i.text]
    return pars

@logger
def show_content(stripped_content):
    system('clear')
    sleep(2)

    print(f"\t\t\t\tDaily devotional for {DATE}\n")
    print(f"{stripped_content[0]}\n\t\t\t\t\t\t\t\t\t\t~ {stripped_content[1]}\n\n")

    for i in stripped_content[2:-1]:
        print(i + "\n")
    
    print(f"Scripture Reading: {stripped_content[-1]}")
    return stripped_content[-1]

@logger
def check_multiple_verses(verse):
    if ";" in verse:
        verses = verse.split(";")
        return [x.replace(" ", "") for x in verses]
    else: return [verse]

@logger
def get_scripture(verse_list):
    verses = dict()

    for verse in verse_list:
        components = verse.split(" ")
        if len(components) == 2:
            book = components[0]
            chapter = components[1].split(":")[0]
            verse_range = components[1].split(":")[1]
            verse_url = f"https://www.biblegateway.com/passage/?search={book}+{chapter}%3A{verse_range}&version=AMP"
            verses[verse_url] = verse_range
        else:
            book_num = components[0]
            book = components[1]
            chapter = components[2].split(":")[0]
            verse_range = components[2].split(":")[1]
            verse_url = f"https://www.biblegateway.com/passage/?search={book_num}+{book}+{chapter}%3A{verse_range}&version=AMP"
            verses[verse_url] = verse_range

    return verses

def get_verse_text(verse_dict):
    
    verse_list = list()

    for verse_url, verse_range in verse_dict.items():
        verse_html = get_html(verse_url)
        start = int(verse_range.split("-")[0])
        end = int(verse_range.split("-")[1])
        v_range = [i for i in range(start, end + 1)]

        soup = BeautifulSoup(verse_html, 'html.parser')
        spans = soup.findAll('span')

        verses = list()
        for s in spans:
            verse_number = s.text.split(" ")[0]        
            for v in v_range:
                if str(v) in verse_number and s.text != "":
                    verses.append(str(s.text))
    
        rem_dups = list()
        for index, verse in enumerate(verses):
            if index > 0:
                test = verse.split(" ")[0]
                if test == verses[index - 1].split(" ")[0]: continue
                else: rem_dups.append(verse)
        verse_list.append(rem_dups)

    return verse_list

def show_passage(verse_list, content_list):
    system("clear")
    sleep(1)
    
    for x in len(verse_list):
        print(f"\t\t\t\t*~~~~<|{verse_list[x]}|>~~~~*\n")
        print(content_list[x] + "\n")
        print()

if __name__ == '__main__':
    html = get_html(F2F)
    content = get_content(html)
    stripped_content = strip_content(content)
    verse = show_content(stripped_content)

    continue_key = input("\nPress any key to continue...")
    
    verse_list = check_multiple_verses(verse)
    verse_dict = get_scripture(verse_list)
    
    passages = get_verse_text(verse_dict)
    show_passage(verse_list, passages)
	
