#!/usr/bin/env python
import logging

if __name__ == '__main__':

    # You can write log messages to a file like this:

    logging.basicConfig(
        level=logging.DEBUG,
        filename="./app.log", 
        filemode="a",
        format="%(name)s - %(levelname)s - %(message)s",
    )

    logging.debug("this will get written to the log file...")
    logging.warning("this will also get written to the log file")