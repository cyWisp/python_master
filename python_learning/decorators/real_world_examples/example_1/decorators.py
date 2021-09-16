#!/usr/bin/env python
import logging

def configure_logging():
    format = "%(process)d - %(asctime)s: %(message)s"
    logging.basicConfig(
        format=format,
        datefmt="%H%M%S",
        level=logging.INFO,
        handlers=[logging.StreamHandler()]
    )
    

def deco(func):
    def wrapper(*args, **kwargs):
        print("The sum is: ")
        value = func(*args, **kwargs)
        return value
    return wrapper

def logging_deco(func):
    def wrapper(*args, **kwargs):
        print("Logging value...")
        value = func(*args, **kwargs)
        logging.info(f"value: {value}")
        return value
    return wrapper


