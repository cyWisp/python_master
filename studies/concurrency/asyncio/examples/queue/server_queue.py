#!/usr/bin/env python
from aiohttp import web
import asyncio
import logging
import sys
import os

logging.basicConfig(
    format='%(process)d - %(asctime)s - %(funcName)s - %(levelname)s: %(message)s',
    datefmt='%m-%d-%Y %H:%M:%S',
    level=logging.DEBUG,
    handlers=[
        logging.StreamHandler(sys.stdout),
    ]
)


routes = web.RouteTableDef()
q = asyncio.Queue()

async def generate_random_string():
    return os.urandom(5).hex()

async def produce(q):
    random_string = await generate_random_string()
    logging.info(f'Adding random string: {random_string} to queue.')

    await q.put(random_string)

async def consume(q):
    new_string = await q.get()
    logging.info(f'String: {new_string}')
    q.task_done()

@routes.get('/tester')
async def handler(request):
    logging.info(f'Incoming request: {request.url}')

    query_string = request.query['num']

    prod = [asyncio.create_task(produce(q)) for i in range(int(query_string))]
    con = [asyncio.create_task(consume(q)) for j in range(len(prod) + 5)]

    await asyncio.gather(*prod)
    await q.join()

    for c in con:
        c.cancel()

    return web.Response(text=f'Processing: {query_string}\n\r')

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)