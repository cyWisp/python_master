#!/usr/bin/env python
import logging

if __name__ == '__main__':

    # Create a custom logger
    logger = logging.getLogger(__name__)

    # Create handlers
    handler = logging.FileHandler('./file.log', 'w', "utf-8")
    s_handler = logging.StreamHandler()
    
    handler.setLevel(logging.WARNING)
    s_handler.setLevel(logging.DEBUG)

    # Create formatters and add it to handlers
    handler_format = logging.Formatter("%(name)s - %(message)s")
    handler.setFormatter(handler_format)
    
    s_handler_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    s_handler.setFormatter(s_handler_format)

    # Add handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(s_handler)
    
    logger.warning("this is a warning")
    logger.debug("this is debug")