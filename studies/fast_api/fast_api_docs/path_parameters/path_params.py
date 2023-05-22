#!/usr/bin/env python
import uvicorn
import logging
from fastapi import FastAPI
from fastapi.exceptions import HTTPException

logging.basicConfig(
    level=logging.INFO,
    format='%(process)d - %(asctime)s - %(filename)s '
    ' - %(funcName)s - %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler()]
)

log = logging.getLogger()
app = FastAPI()

books = {
    'first': {
        1: {
            1: 'some text',
            2: 'some text',
            3: 'some text'
        },
        2: {
            1: 'some text',
            2: 'some text',
            3: 'some text'
        }
    },
    'second': {
        1: {
            1: 'some text',
            2: 'some text',
            3: 'some text'
        },
        2: {
            1: 'some text',
            2: 'some text',
            3: 'some text'
        }
    },
    'third': {
        1: {
            1: 'some text',
            2: 'some text',
            3: 'some text'
        },
        2: {
            1: 'some text',
            2: 'some text',
            3: 'some text'
        }
    }
}


def validate_range(
        book: str,
        chapter: int,
        verse_id: str
):
    if verse_id.isnumeric():
        return int(verse_id)

    if '-' not in verse_id:
        raise TypeError

    list_int_range = [int(verse_id) for verse in verse_id.split('-') if int(verse) in books[book][chapter].keys()]

    if len(list_int_range) != 2:
        raise KeyError


@app.get('/books/{book_name}/{chapter_id}/{verse_id}')
def bible(book_name: str, chapter_id: int, verse_id: str):
    log.info(f'Book: {book_name} | Chapter: {chapter_id} | Verse: {verse_id}')
    log.info(f'{type(book_name)} | {type(chapter_id)} | {type(verse_id)}')

    try:
        return {'message': books[book_name][chapter_id][verse_id]}

    except KeyError:
        log.error(f'Record for /books/{book_name}/{chapter_id}/{verse_id} not found.')
        raise HTTPException(status_code=404, detail='Item not found.')


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8081,
        log_config=None
    )
