from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn

app = FastAPI()

security = HTTPBasic()


@app.get('/users/me')
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {'username': credentials.username, 'password': credentials.password}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)