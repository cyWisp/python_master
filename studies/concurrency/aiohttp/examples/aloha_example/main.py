#!/usr/bin/env python
import json
import requests
import logging
import sys

from config import cfg
from aiohttp import web
from xml.etree import ElementTree
from datetime import datetime

logging.basicConfig(
    format='%(process)d - %(asctime)s - %(funcName)s - %(levelname)s: %(message)s',
    datefmt='%m-%d-%Y %H:%M:%S',
    level=cfg.log_level,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(cfg.log_file, 'a+', 'utf-8')
    ]
)

TODAY = datetime.strptime(datetime.strftime(datetime.today(), cfg.date_format), cfg.date_format)
routes = web.RouteTableDef()


async def forward_request(payload):
    new_request = f'http://localhost:{cfg.forwarding_port}/instore/posXml?activity=IncomingXML&XMLData={payload}'

    logging.info(f'Forwarding request: {new_request}')

    try:
        response = requests.get(new_request)
        logging.info(f'Status code: {response.status_code}\nContent: {response.content}')

        return response.status_code
    except (
        requests.exceptions.ConnectionError,
        requests.exceptions.HTTPError,
        requests.exceptions.Timeout
    ) as e:
        logging.error(f'Unable to forward request: {e}')


async def get_correct_date(date_str):
    logging.info(f'Verifying date value: Payload date: {date_str} | Current date: {str(TODAY).split(" ")[0]}')

    try:
        # Convert date string to datetime object
        dt_object = datetime.strptime(date_str, cfg.date_format)

        # Compare payload date to current date
        if dt_object != TODAY:
            logging.info('Updating payload to reflect current date.')
            current_date = datetime.strftime(TODAY, cfg.date_format)
        else:
            logging.info('Dates match. Nothing to do ¯\_(ツ)_/¯')
            current_date = date_str

        return current_date

    except Exception as e:
        logging.error(f'Conversion/Comparison failed: {e}')


async def modify_xml(payload):
    logging.info('Extracting date value.')

    try:
        xml_data = ElementTree.fromstring(payload['XMLData'])
        date = xml_data.find('Date')

        date.text = await get_correct_date(date.text)
        xml_str = ElementTree.tostring(xml_data, encoding='unicode', method='xml')

        return xml_str

    except Exception as e:
        logging.error(f'Unable to extract date: {e}')


@routes.get('/instore/posXml')
async def handler(request):
    logging.info(f'Incoming request on port {cfg.listening_port}.')

    modified = await modify_xml(request.query)
    status_code = await forward_request(modified)

    if status_code == 200:
        logging.info('Request successful.')
        return web.Response(text='Request forwarding succeeded.')
    else:
        logging.info('Request failed.')
        return web.Response(text='Request forwarding failed.')


app = web.Application()
app.add_routes(routes)

logging.info(json.dumps(vars(cfg), indent=4))

if __name__ == '__main__':
    web.run_app(app, port=cfg.listening_port)
