#!/usr/bin/env python
from aiohttp import web
import logging

logging.basicConfig(
    format='%(process)d - %(levelname)s - %(funcName)s: %(message)s',
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)

async def handler(request):
    logging.info(f'Incoming request: {request.url}')
    return web.Response(text="Got it.")

app = web.Application()
app.add_routes([
    web.get('/test_get', handler),
    web.put('/test_put', handler)
])

if __name__ == '__main__':
    web.run_app(app)
