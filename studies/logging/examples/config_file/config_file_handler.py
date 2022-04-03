#!/usr/bin/env python
import logging
import logging.config

if __name__ == '__main__':
    logging.config.fileConfig(fname="./app.conf", disable_existing_loggers=False)

    # Get the logger specified in the file
    logger = logging.getLogger(__name__)

    logger.debug("this is a debug message")