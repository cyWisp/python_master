from fastapi import FastAPI
from enum import Enum

class Users:
    users = {
        'Rob': 'rob123',
        'Sam': 'samIsCool',
        'Beth': 'beth777'
    }

app = FastAPI()

@app.get('/all')
def get_all_users():
    return {'all': Users.users}

@app.get('/users/{name}')
def get_user_name(name):
    if name in Users.users:
        return {'username': Users.users[name]}


