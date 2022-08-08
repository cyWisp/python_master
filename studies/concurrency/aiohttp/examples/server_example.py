#!/usr/bin/env python
from aiohttp import web
import asyncio

async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = f'Hello {name}'
    return web.Response(text=text)

async def xml_handler(request):
    payload = request.match_info.get('payload', '<empty>')
    text = f'payload: {payload}'
    return web.Response(text=text)

app = web.Application()
app.add_routes([
    web.get('/', handle),
    web.get('/{name}', handle),
    web.get(f'/instore/posXml?activity=IncomingXML&XMLData={payload}', xml_handler)
])

if __name__ == '__main__':
    web.run_app(app)
