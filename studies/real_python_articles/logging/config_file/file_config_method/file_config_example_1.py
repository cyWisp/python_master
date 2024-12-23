#!/usr/bin/env python
import logging
import logging.config

logging.config.fileConfig(fname='./logger.conf', disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
