from fastapi import FastAPI
from enum import Enum

class Users(dict, Enum):
    users = {
        'Rob': 'rob123',
        'Alex': 'al15',
        'Tom': 'tommyboy12'
    }

app = FastAPI()

@app.get('/users/{name}')
def get_user_name(name: str):
    if name in Users.users.value.keys():
        return {
            'Name': name,
            'Username': Users.users.value[name]
        }



