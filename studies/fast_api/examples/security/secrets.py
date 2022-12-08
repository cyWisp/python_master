import hashlib
import uvicorn

from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
    status
)

from fastapi.security import HTTPBasic, HTTPBasicCredentials

USER = b'apiUser'
PASS = b'password'

app = FastAPI()
security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    is_correct_username = (hashlib.sha256(credentials.username.encode('utf-8')).hexdigest() ==
                           hashlib.sha256(USER).hexdigest())

    is_correct_password = (hashlib.sha256(credentials.password.encode('utf-8')).hexdigest() ==
                           hashlib.sha256(PASS).hexdigest())

    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password.',
            headers={'WWW-Authenticate': 'Basic'}
        )

    return credentials.username


@app.get('/users/me')
def read_current_user(username: str = Depends(get_current_username)):
    return {'username': username}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)