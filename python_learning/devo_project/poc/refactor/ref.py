#!/usr/bin/env python
import requests, logging, json
from bs4 import BeautifulSoup
from sys import argv, exit

BOOK_MAPPINGS = "./book_mappings.json"

logging.basicConfig(
    format = "%(process)d - %(asctime)s: %(message)s",
    level = logging.INFO,
    datefmt = "%H:%M:%S",
    handlers = [logging.FileHandler("./app.log", "w", "utf-8")]
)

def get_html(url): return requests.get(url).text

def get_book_mappings():
    try:
        with open(BOOK_MAPPINGS, 'r') as bm:
            book_mappings = json.load(bm)
    except Exception as e: print(f"[x] Error: {e}")
    else: return book_mappings

def find_verses(verse_info):
    html = get_html(verse_info['url'])
    soup = BeautifulSoup(html, 'html.parser')
    verse_list = list()
    
    if verse_info['mult']:
        for v in verse_info['verse_range']:
            span_name = f'{verse_info["abr"]}-{verse_info["chapter"]}-{v}'
            verse_span = soup.findAll("span", {"class": f"text {span_name}"})
            for v in verse_span: verse_list.append(v.text)
    else:
        verse_span = soup.findAll("span", {"class": f"text {verse_info['span_name']}"})
        for v in verse_span:
            try: verse_num = int(v.text[0])
            except (ValueError, TypeError): continue
            else: verse_list.append(v.text)
    
    return verse_list

def get_verse(book, verse, book_mappings):
    mult = False
    abr = book_mappings[book]
    chapter = verse.split(":")[0]
    verses = verse.split(":")[1]
    
    logging.info(f"\n\tmult: {mult}\n\tabr: {abr}\n\tchapter: {chapter}\n\tverses: {verses}")

    if "-" in verses:
        mult = True
        first = int(verses.split("-")[0])
        last = int(verses.split("-")[1]) + 1
        verse_range = [x for x in range(first, last)]
        url = f"https://www.biblegateway.com/passage/?search={book}+{chapter}%3A{first}-{last}&version=AMP"
        
        logging.info(f"\n\tfirst: {first}\n\tlast: {last}\n\tverse_range: {verse_range}\n\turl: {url}")
        return {
            'mult': mult, 
            "abr": abr,
            "chapter": chapter,
            "verse_range": verse_range, 
            "url": url
        }
    else:
        url = f"https://www.biblegateway.com/passage/?search={book}+{chapter}%3A{verses}&version=AMP"
        span_name = f"{abr}-{chapter}-{verses}"
        logging.info(f"\n\tspan_name: {span_name}\n\turl: {url}")
        return {
            "mult": mult,
            "url": url, 
            "span_name": span_name
        }

if __name__ == '__main__':
    if len(argv) != 3:
        print(f"[x] Usage: python {argv[0]} <verse [chapter]:[verse/verse_range (x-n)]>")
        exit()

    book_mappings = get_book_mappings()
    logging.info(book_mappings)

    if " " in argv[1]: book_name = argv[1].replace(" ", "")
    else: book_name = argv[1]

    verse_info = get_verse(book_name, argv[2], book_mappings)
    verses = find_verses(verse_info)

    for v in verses: print(v)

    # test_url = "https://www.biblegateway.com/passage/?search=Genesis+1%3A1&version=AMP"
    # html = requests.get(test_url).text

    # verses = find_verses("Genesis 1:1", html)
    # for v in verses:
    #     print(v)