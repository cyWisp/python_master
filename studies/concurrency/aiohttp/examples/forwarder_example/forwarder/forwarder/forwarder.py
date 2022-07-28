from aiohttp import web
import asyncio
import logging

logging.basicConfig(
    format='%(process)d - %(levelname)s - %(funcName)s: %(message)s',
    level=logging.getLevelName(logging.INFO),
    handlers=[logging.StreamHandler()],
)

q = asyncio.Queue()

async def start_server():
    routes = web.RouteTableDef()

    @routes.get('/forward')
    async def request_handler(request):
        try:
            name = request.query['name']
            await q.put(name)

            return web.Response(text=f'Hi {name}\n\r')
        except KeyError as e:
            logging.error(f'Caught it! {e}')

    app = web.Application()
    app.add_routes(routes)

    web.run_app(app)

async def print_name():
    while True:
        name = await q.get()
        logging.info(f'Person: {name}')

async def main():
    try:
        tasks = [start_server(), print_name()]
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        logging.error('this definitely didnt work.')

if __name__ == '__main__':
    asyncio.run(main())