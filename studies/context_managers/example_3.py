#!/usr/bin/env python
import logging

logging.basicConfig(
    level=logging.INFO
)
log = logging.getLogger()


class Example:
    def __init__(self, name, age, location) -> None:
        self.name, self.age, self.location = name, age, location

    def __str__(self):
        return self.__dict__

    def __enter__(self):
        return self

    def get_info(self):
        log.info(self.__dict__)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass


if __name__ == '__main__':

    with Example('Rob', '37', 'Miami') as ex:
        log.info(ex)
        ex.get_info()
