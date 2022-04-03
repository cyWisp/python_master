#!/usr/bin/env python
import logging

def create_logger(name):
    f_logger = logging.getLogger(name)

    f_handler = logging.FileHandler("./app.log", 'a+', 'utf-8')
    f_handler.setLevel(logging.WARNING)

    f_format = logging.Formatter("%(process)d - %(asctime)s - %(name)s: %(message)s")
    f_handler.setFormatter(f_format)

    f_logger.addHandler(f_handler)

    return f_logger

def log_list(logger, var):
    logger.warning(f"List Contents: {var}")

def log_dict(logger, dict_var, name):
    logger.warning(f"Name: {name}")
    for k, v in dict_var.items():
        logger.warning(f"key: {k}")
        logger.warning(f"values: {v}")
        
