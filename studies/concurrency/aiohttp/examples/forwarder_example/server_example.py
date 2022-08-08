#!/usr/bin/env python
from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/test')
async def handler(request):
    q = request.query['name']
    text = f'Hi {q}'

    return web.Response(text=text)


app = web.Application()
app.add_routes(routes)

if __name__ == '__main__':
    web.run_app(app)

