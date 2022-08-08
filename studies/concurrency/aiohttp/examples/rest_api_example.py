#!/usr/bin/env python
from aiohttp import web
from xml.etree import ElementTree
import logging

logging.basicConfig(
    format='%(message)s',
    level=logging.INFO
)
log = logging.getLogger()

routes = web.RouteTableDef()

def modify_xml(payload):
    xml_data = ElementTree.fromstring(payload['XMLData'])
    date = xml_data.find('Date')
    date.text = 'Edited'
    # date = xml_data.findall('Date')[0].text
    return date.text

@routes.get('/instore/posXml')
async def handler(request):

    modified = modify_xml(request.query)

    # xml_data = ElementTree.fromstring(request.query['XMLData'])
    # xml_str = q['XMLData']

    # parsed = ElementTree.fromstring(xml_str)
    # date = parsed.findall('Date')

    # date = ElementTree.fromstring(xml_data).findall('Date')[0].text

    return web.Response(text=str(modified))

    # date_str = re.findall('<Date>(.*)</Date>', url_decoded)

app = web.Application(logger=log)
app.add_routes(routes)


if __name__ == '__main__':
    web.run_app(app, port=8083)
