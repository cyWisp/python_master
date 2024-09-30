import configparser

import configargparse
import jwt
import json


parser = configargparse.get_argument_parser(
    description='Arguments for JWT encoder/decoder'
)

parser.add_argument('-l', '--log-level', default='INFO)



class PyJWT:
    def __init__(
        self
    ):
        pass



if __name__ == '__main__':
    token = jwt.encode(
        payload=payload_data,
        key=my_secret
    )

    print(token)