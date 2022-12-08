from fastapi import FastAPI, Request


items = [
    {'name': 'rob'},
    {'name': 'sam'},
    {'name': 'pete'},
    {'name': 'will'},
    {'name': 'tom'}
]

app = FastAPI()

@app.get("/items")
async def get_name(skip: int = 0, limit: int = None):
    if limit:
        return items[skip:skip+limit]
    return items[skip:]
