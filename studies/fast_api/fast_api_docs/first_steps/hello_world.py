#!/usr/bin/env python
import uvicorn
import logging
from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO,
    format='%(process)d - %(asctime)s - %(filename)s '
    ' - %(funcName)s - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler()]
)

app = FastAPI()


@app.get('/')
def index():
    return {'message': 'hello, world!'}


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8081,
        log_config=None
    )
