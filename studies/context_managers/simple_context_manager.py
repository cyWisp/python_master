#!/usr/bin/env python
import logging
import json

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


class Simple:
    def __init__(
        self,
        name: str,
        age: int,
        location: str
    ) -> None:
        self.name, self.age, self.location = name, age, location

    def __str__(self):
        return self.__dict__

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def greet(self):
        return f'Hello, my name is {self.name}' \
               f', I am {self.age} years old.' \
               f' I am from {self.location}.'


if __name__ == '__main__':
    with Simple('Rob', 37, 'Miami') as s:
        log.info(json.dumps(s.__str__(), indent=4))
        log.info(s.greet())
