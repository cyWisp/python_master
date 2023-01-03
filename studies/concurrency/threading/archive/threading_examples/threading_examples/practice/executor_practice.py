#!/usr/bin/env python
import requests, logging, concurrent.futures, threading, time
from bs4 import BeautifulSoup

logging.basicConfig(
    format="%(process)d - %(asctime)s - %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)

URLS = [
    "http://cybersherpa.net",
    "https://example.com"
]

def get_titles(index, url, thread_lock):
    with thread_lock:
        logging.info(f"Thread {index} starting...")
        logging.debug(f"Thread {index} has lock...")

        site_name = url.split("/")[-1].split(".")[0]
        html = requests.get(url).text
    
        time.sleep(0.1)
        title = BeautifulSoup(html, 'html.parser').find('title').getText()
        
        logging.debug(f"Thread {index} about to realease lock...")

    logging.debug(f"Thread {index} after release...")
    logging.info(f"Thread {index} returning...")
    return (site_name, title)

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    thread_lock = threading.Lock()
    results = list()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for index, url in enumerate(URLS):
            future = executor.submit(get_titles, index, url, thread_lock)
            results.append(future.result())

    for r in results: print(f"{r[0]}: {r[1]}")

