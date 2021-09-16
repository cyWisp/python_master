#!/usr/bin/env python
import logging
from log_module import create_logger, log_dict

def test_function_2(var):

    # log_warning = create_logger(__name__, logging.WARNING)
    # log_warning.warning("this is a warning")

    log_warning = create_logger(__name__)
    
    log_dict(log_warning, var, "some dict")