#!/usr/bin/env python
import json, logging
from books import get_abr

LOG_FILE = "./logs/main.log"
ABRS = "./data/book_mappings.json"

logging.basicConfig(
    format ="%(process)d - %(asctime)s: %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler('LOG_FILE', 'w', 'utf-8'),
        logging.StreamHandler()
    ]
)

def read_abrs():
    logging.debug("Reading book mappings...")
    try:
        with open(ABRS, 'r') as book_mappings:
            abrs = json.load(book_mappings)
    except Exception as e: logging.debug(f"ERROR: {e.__class__.__name__}: {e}")
    else: return abrs

if __name__ == '__main__':
    book = "Genesis"
    abrs = read_abrs()

    for book, abr in abrs.items():
        logging.debug(f"{book}: {abr}")

    # get_abr.update_abrs()


