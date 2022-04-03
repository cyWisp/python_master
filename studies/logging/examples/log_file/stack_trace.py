#!/usr/bin/env python
import logging
from logging import info, INFO, basicConfig, FileHandler

PATH = "./app.log"

def configure_logging(path):
    format = "%(process)d - %(asctime)s: %(message)s"
    basicConfig(
        format=format,
        datefmt="%H:%M:%S",
        level=INFO,
        handlers=[FileHandler(path, 'w', "utf-8")],
    )

if __name__ == '__main__':
    configure_logging(PATH)

    # Log the full stack trace
    try:
        c = 1 / 0
    except Exception as e:
        logging.error("[x] Error: ", exc_info=True)
    
    # If logging from an exception handler, use logging.exception()
    try:
        c = 1 / 0
    except Exception as e:
        logging.exception("[x] Error:")

    print("got here")