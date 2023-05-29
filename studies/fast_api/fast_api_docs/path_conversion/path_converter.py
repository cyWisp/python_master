#!/usr/bin/env python
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    with open(file_path) as f:
        content = f.read()

    return {'file_content': content}

if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8081,
    )