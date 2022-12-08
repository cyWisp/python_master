from fastapi import FastAPI, Request
import uvicorn
import asyncio

app = FastAPI()

class Endpoint:
    @staticmethod
    @app.post('/index/{param}')
    async def handler(param: dict):
        return {'Result': param}

new_endpoint = Endpoint()


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8084)