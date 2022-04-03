#!/usr/bin/env python
import logging

if __name__ == '__main__':

    # You can use the basicConfig(**kwargs) method to configure logging
    # parameters:
    # level: the root logger wil be set to the specified severity level
    # filename: this specifies an output file
    # filemode: if filename is given, the file is opened
    #     in this mode. The default is a, which means append.
    # format: this is the format of the log message

    logging.basicConfig(level=logging.DEBUG)

    # All events at or above DEBUG level will now be logged
    logging.debug("This will get logged")
    logging.error("This will also get logged...")

    