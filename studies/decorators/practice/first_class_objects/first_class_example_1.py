#!/usr/bin/env python
import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


if __name__ == '__main__':
    log.info(greet_bob(be_awesome))