from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

import logging

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

app = FastAPI()

class Tester:
    @app.post('/items/')
    async def create_item(self, item: Item):
        return item

new_tester = Tester()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8084)