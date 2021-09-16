#!/usr/bin/env python
import logging

if __name__ == '__main__':

    """
    It is recommended that we use module-level loggers by passing
    __name__ as the name parameter to getLogger() to create a logger
    object as the name of the logger itself would tell us from
    where the events are being logged.
    __name__ is a special built-in variable in Python which
    evaluates to the name of the current module.
    """

    logger = logging.getLogger('example_logger')
    logger.warning("This is a warning..")