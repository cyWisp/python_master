from aiohttp import web
from xml.etree import ElementTree
import logging

logging.basicConfig(
    format='%(message)s',
    level=logging.INFO
)
log = logging.getLogger()

routes = web.RouteTableDef()


def get_date(payload):
    xml_data = ElementTree.fromstring(payload['XMLData'])
    date = xml_data.find('Date')
    date.text = f'New date: {date.text}'

    return date.text


@routes.get('/instore/posXml')
async def handler(request):
    date_str = get_date(request.query)
    return web.Response(text=str(date_str))

app = web.Application(logger=log)
app.add_routes(routes)


if __name__ == '__main__':
    web.run_app(app, port=9999)