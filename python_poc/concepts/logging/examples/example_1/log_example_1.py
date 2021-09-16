#!/usr/bin/env python
import logging

def function_1():
    debug_message = "function_1 has run"
    return  debug_message

def function_2():
    debug_message = "function_2 has run"
    return  debug_message

if __name__ == '__main__':

    # log file name constant
    # and logging configuration
    LOG_FILENAME = './log.txt'
    logging.basicConfig(
        filename=LOG_FILENAME,
        level=logging.DEBUG,
    )

    function_result_1 = function_1()
    function_result_2 = function_2()

    logging.debug(function_result_1)
    logging.debug(function_result_2)
    logging.debug('the program terminated successfully...')

    print("[*] Done...")
