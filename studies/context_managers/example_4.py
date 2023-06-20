#!/usr/bin/env python
import logging
import json

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

class Example:
    def __init__(self, name: str, age: int, location: str) -> None:
        self.name, self.age, self.location = name, age, location

    def __enter__(self):
        return self

    def __str__(self):
        return json.dumps(self.__dict__, indent=4)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass


if __name__ == '__main__':
    new_example = Example('Rob', 37, 'Miami')
    log.info(new_example.__str__())


    with Example('Rob', 37, 'Miami') as ex:
        log.info(ex.__str__())

