#!/usr/bin/env python

import logging
from logging import info, INFO, basicConfig, FileHandler

def configure_logging(path):
    format = "%(process)d - %(asctime)s: %(message)s"
    basicConfig(
        format=format,
        datefmt="%H:%M:%S",
        level=INFO,
        handlers=[FileHandler(path, 'w', "utf-8")],
    )

def log_dict(d, dict_name):
    info(f"*** {dict_name} ***\n")
    for k, v in d.items():
        info(f"[+] Key: {k}")
        info(f"[+] Values: {v}")
        info("\n")
    info(f"*** End {dict_name} ***\n")

def log_nested(d, dict_name):
    info(f"*** {dict_name} ***")
    for k, v in d.items():
        info(f"[+] Key: {k}")
        for i in v:
            info(f"[+] Nested list: {i}")
        info("\n\n")
    info(f"*** End {dict_name} ***\n")
    
def log_count(d, dict_name):
    info(f"Item count: {len(d)}")
    for k, v in d.items():
        info(f"Parent List Length: {len(v)}")
        for i in v:
            info(f"List Length: {len(i)}\n{i}\n")
        info("\n")
    info("CI Functions Processed:")
    for k in d.keys():
        info(k)
