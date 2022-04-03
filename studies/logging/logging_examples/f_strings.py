#!/usr/bin/env python
import logging

if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG)

    var = "test var"

    # F strings don't work
    logging.debug("var: " + var)