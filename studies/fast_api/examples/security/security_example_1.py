from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
import uvicorn

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

@app.get('/items/')
async def read_items(token: str = Depends(oauth2_scheme)):
    return {'token': token}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)