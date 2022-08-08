#!/usr/bin/env python
from aiohttp import web
import asyncio
import logging
import sys

logging.basicConfig(
    format='%(process)d - %(funcName)s: %(message)s',
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()]
)

routes = web.RouteTableDef()

class DoStuff:
    def __init__(self):
        self.q = asyncio.Queue()

    async def append_to_queue(self, query_string):
        await self.q.put(query_string)

    async def process_queue(self):
        queue_item = await self.q.get()
        logging.info(f'Queue item: {queue_item}')
        self.q.task_done()

new_task_handler = DoStuff()

@routes.get('/test')
async def handler(request):
    logging.debug(f'Incoming request: {request.url}')

    query_string = request.query['num']

    new_task = asyncio.create_task(new_task_handler.append_to_queue(query_string))
    new_queue_process = asyncio.create_task(new_task_handler.process_queue())

    await asyncio.gather(new_task, new_queue_process)
    await new_task_handler.q.join()

    return web.Response(text=f'Processing: {query_string}\n\r')

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app, port=9999)