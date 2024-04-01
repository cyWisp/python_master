import time
import redis
import logging

from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


def get_hit_count():
    retries = 5

    while True:
        try:
            return cache.incr('hits')

        except redis.exceptions.ConnectionError as e:
            if not retries:
                raise e

            retries -= 1
            time.sleep(0.5)


@app.route('/')
@app.route('/index')
def report_hit_count():
    count = get_hit_count()

    response = f'''<!doctype html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Document</title>
        <link rel="stylesheet" href="">
        <style>
            .red {{
                color: red;
            }}
        </style>
    </head>
    <body>
        <p>This page has been viewed <span class="red">{count}</span> times.</p>
        <p>This is another paragraph.</p>

        <script src="" type=""></script>
    </body>
    </html>
    '''

    return response


# if __name__ == '__main__':
#     app.run(
#         host='0.0.0.0',
#         port=5000
#     )
