#!/usr/bin/env python
import logging
from enum import Enum
from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO,
    format='%(process)d - %(asctime)s - %(filename)s '
    ' - %(funcName)s - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler()]
)

log = logging.getLogger()


class ModelName(str, Enum):
    first = 'first'
    second = 'second'
    third = 'third'


if __name__ == '__main__':
    var = 'first'

    log.info(type(ModelName.first.value))
