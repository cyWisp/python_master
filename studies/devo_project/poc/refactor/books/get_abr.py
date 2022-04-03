#!/usr/bin/env python
import json, requests, asyncio, logging
from bs4 import BeautifulSoup
from sys import exit

# LOG_FILE = "./logs/abr_updater.log"
LOG_FILE = "./app.log"

logging.basicConfig(
    format="%(process)d - %(asctime)s: %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler(LOG_FILE, 'w', 'utf-8'),
        logging.StreamHandler()
    ]
)

BOOKS = "./data/books.json"
BOOK_ABRS = "./data//book_mappings.json"

def read_books(file_name):
    logging.debug(f"Reading books from {file_name}")
    try:
        with open(file_name, 'r') as b:
            books = json.load(b)
    except BaseException as e:
        print(f"[x] Error: {e}\n")
        exit()

    for book in books: logging.debug(f"Book: {book}")
    return books

def write_book_abrs(book_abrs):
    logging.debug(f"Writing book abbreviations to {BOOK_ABRS}")
    try:                
        with open(BOOK_ABRS, 'w') as ba:
            json.dump(book_abrs, ba)
    except Exception: print("[x] Error")  

def convert_to_dict(abrs_list):
    logging.debug(f"Converting list of tuples to dict...")
    return {x[0]: x[1] for x in abrs_list}

async def update_book_mappings(book):
    logging.debug(f"Starting coroutine for {book}")

    abr = ""
    name = book

    try: book_num = int(book[0])
    except Exception: pass
    else: book = book.replace(" ", "")

    url = f"https://www.biblegateway.com/passage/?search={book}+1%3A1&version=AMP"
    response = requests.get(url)

    logging.debug(f"Reponse code: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    span_classes = soup.findAll('span', class_=True)

    await asyncio.sleep(1)

    for s in span_classes:
        for i in s['class']:
            if book[:3] in i or book[:4] in i: abbr = i.split("-")[0]
    
    return (name, abr)

async def main(*args):
    res = await asyncio.gather(*(update_book_mappings(b) for b in args))
    return res

def update_abrs():
    books = read_books(BOOKS)
    abrs = asyncio.run(main(*books))
    abrs_dict = convert_to_dict(abrs)
    write_book_abrs(abrs_dict)

if __name__ == '__main__':
    update_abrs()

    
