#!/usr/bin/env python
from config import cfg
from forwarder.forwarder import app, q
from aiohttp import web
import json
import logging
import asyncio


logging.basicConfig(
    format='%(process)d - %(levelname)s - %(funcName)s: %(message)s',
    level=logging.getLevelName(cfg.log_level),
    handlers=[logging.StreamHandler()],
)

logging.info(json.dumps(vars(cfg), indent=4))

async def say_hi():
    while True:
        person = await q.get()
        logging.info(f'Shout out to {person}.')



if __name__ == '__main__':
    logging.info('This is a test... do we suck?')
    logging.debug('this is a debug message.')


