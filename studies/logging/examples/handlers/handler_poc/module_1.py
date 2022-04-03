#!/usr/bin/env python
import logging
from log_module import create_logger

def test_function_1():
    logger = create_logger(__name__, logging.ERROR)
    logger.error("this is an error")