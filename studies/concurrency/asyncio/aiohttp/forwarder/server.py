#!/usr/bin/env python
from aiohttp import web
import logging

logging.basicConfig(
    format='%(process)d - %(funcName)s: %(message)s',
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)

routes = web.RouteTableDef()

@routes.get('/endpoint')
async def handler(request):
    name = request.query['name']

    return web.Response(text=f'Name: {name}\n\r')

app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)