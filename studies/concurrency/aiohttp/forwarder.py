#!/usr/bin/env python
from aiohttp import web, ClientSession
import asyncio
import logging

logging.basicConfig(
    format='%(process)d - %(levelname)s - %(funcName)s: %(message)s',
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)

class Forwarder:
    def __init__(self):
        self.process_queue = asyncio.Queue()

    async def handler(self, request):

        logging.info(f'Request received: {request.url}')
        await self.process_queue.put(request.query['name'])

        process_task = asyncio.create_task(self.process_name())
        await asyncio.gather(process_task)
        await self.process_queue.join()


        return web.Response(text='got it\n\r')

    async def forward_name(self, name):
        try:
            logging.info('Forwarding request.')

            async with ClientSession() as session:
                async with session.get(f'http://localhost:8080/test_get?name={name}') as response:
                    logging.info(f'Status: {response.status}')
                    return await response.text()

        except Exception as e:
            logging.exception(e)

    async def process_name(self):
        name = await self.process_queue.get()
        response = await self.forward_name(name)
        logging.info(f'Server response: {response}')
        self.process_queue.task_done()


app = web.Application()
handler = Forwarder()
app.add_routes([
    web.get('/get_name', handler.handler),
    web.put('/put_name', handler.handler)
])

if __name__ == '__main__':
    web.run_app(app, port=9999)