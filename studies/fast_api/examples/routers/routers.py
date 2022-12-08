import asyncio
import uvicorn
import logging
import json

from fastapi import FastAPI
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi.encoders import jsonable_encoder
from typing import Union
from pydantic import BaseModel


logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.DEBUG
)

log = logging.getLogger()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

router = InferringRouter()

@cbv(router)
class Tester:
    def __init__(self):
        in_queue, out_queue = asyncio.Queue(), asyncio.Queue()

    @router.post('/items/')
    def create_item(self, item: Item) -> Item:
        item_json = jsonable_encoder(item)
        log.debug(type(item_json))
        log.debug(json.dumps(item_json, indent=4))

        return item


if __name__ == '__main__':
    log.debug('this is a test')


    app = FastAPI()
    app.include_router(router)

    uvicorn.run(app, host='0.0.0.0', port=8084, log_config=None)

