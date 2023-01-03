import hashlib
import uvicorn
import logging

from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
    status
)

from fastapi.security import HTTPBasic, HTTPBasicCredentials

logging.basicConfig(
    format='%(asctime)s: %(message)s',
    level=logging.DEBUG
)

log = logging.getLogger()

USER = b'apiUser'
PASS = b'password'

app = FastAPI()
security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):

    log.debug(f'Username: {credentials.username}')
    is_correct_username = (hashlib.sha256(credentials.username.encode('utf-8')).hexdigest() ==
                           hashlib.sha256(USER).hexdigest())

    log.debug(f'Password: {credentials.password}')
    is_correct_password = (hashlib.sha256(credentials.password.encode('utf-8')).hexdigest() ==
                           hashlib.sha256(PASS).hexdigest())

    auth = is_correct_username and is_correct_password

    log.debug(f'Authenticated: {auth}')

    if not auth:
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
    log.debug('Starting...')
    uvicorn.run(app, host='0.0.0.0', port=8000, log_config=None)