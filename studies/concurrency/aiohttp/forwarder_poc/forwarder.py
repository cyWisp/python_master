from aiohttp import web, ClientSession
import asyncio
import logging
import configargparse

logging.basicConfig(
    format='%(process)d - %(funcName)s: %(message)s',
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)

log = logging.getLogger()

class CaptainUnderpants:
    async def get_captain_underpants(self, name):
        if name == 'Rob':
            return 'Captain Underpants'
        else:
            return 'Not Captain Underpants'

class Forwarder:
    def __init__(self):
        self.in_queue, self.out_queue = asyncio.Queue(), asyncio.Queue()
        self.captain_underpants = CaptainUnderpants()
        self.result = None

    async def handler(self, request):
        log.info('Request received.')
        log.debug(f'Request URL: {request.url}')
        await self.in_queue.put(request.query['name'])

        try:
            await asyncio.gather(
                self.replace_name(),
                self.forward_request()
            )
            await self.in_queue.join()
            await self.out_queue.join()

            return web.Response(text=f'Hi! {self.result}\n\r')

        except Exception:
            raise web.HTTPBadRequest

    async def replace_name(self):
        name = await self.in_queue.get()
        self.result = await self.captain_underpants.get_captain_underpants(name)

        await self.out_queue.put(self.result)
        self.in_queue.task_done()

    async def forward_request(self):
        name = await self.out_queue.get()

        logging.info('Forwarding request.')

        async with ClientSession() as session:
            async with session.get(f'http://localhost:8080/test_get?name={name}') as response:
                logging.info(f'Status: {response.status}')

        self.out_queue.task_done()

app = web.Application()
handler = Forwarder()
app.add_routes([
    web.get('/get_name', handler.handler),
    web.put('/put_name', handler.handler)
])

if __name__ == '__main__':
    web.run_app(app, port=9999, access_log=None)