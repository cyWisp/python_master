import os
import sys
import logging
import configargparse
import base64
import re
from os.path import expanduser
from datetime import datetime, UTC
import json
from json import JSONEncoder

import boto3
from botocore.exceptions import BotoCoreError
from botocore.exceptions import ClientError

import requests
import defusedxml.ElementTree as dt
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse

from onepassword import OnePassword


parser = configargparse.get_argument_parser(
    description='A script to automate AWS CLI authentication.',
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter
)

parser.add_argument('-l', '--log-level', type=str, required=False, default='info',
                    help='The log level to use.')

parser.add_argument('-f', '--log-file-path', type=str, required=False,
                    default=f'{os.path.join(os.path.expanduser("~"), ".aws/adfs.log")}',
                    help='The log file path.')

parser.add_argument('-r', '--region', type=str, required=False, default='us-east-1',
                    help='The AWS region.')

parser.add_argument('-a', '--arn', type=str, required=True, help='Role ARN')
parser.add_argument('-c', '--cache-file-path', type=str, required=False,
                    default=f'{os.path.join(os.path.expanduser("~"), ".aws/adfs_cache/dev.json")}',
                    help='Cache file to use.')

cfg = parser.parse_known_args()[0]

logging.basicConfig(
    level=logging.getLevelName(cfg.log_level.upper()),
    datefmt='%Y-%m-%d %H:%M:%S',
    format='%(process)d - %(asctime)s - %(filename)s - %(levelname)s: %(message)s',
)

log = logging.getLogger(__name__)
log.debug(f'Configuration: {json.dumps(vars(cfg), indent=4)}')


class AWSCredentialsManager:
    IDENTITY_URL = ('https://sts.qualnet.org/adfs/ls/IdpInitiatedSign'
                    'On.aspx?loginToRp=urn:amazon:webservices')

    def __init__(
        self,
        cache_file_path: str = None,
        ssl_verification: bool = True
    ) -> None:

        self.credentials = self.load_cache(cache_file_path)
        self.parse_cache()

        self.ssl_verification = ssl_verification

    @staticmethod
    def load_cache(cache_file: str) -> dict:
        try:
            log.info('Reading credentials cache file')

            if cache_file:
                with open(cache_file, 'r') as f:
                    return json.load(f)

            raise FileNotFoundError
        except (FileNotFoundError, IOError) as e:
            log.error(e)
            sys.exit(1)

    def parse_cache(self):
        try:
            if datetime.fromisoformat(self.credentials['Expiration']) >= datetime.now(UTC):
                log.info(f'Credentials validated:\n{json.dumps(self.credentials, indent=4)}')
                sys.exit(0)

            log.info('Credentials expired. Fetching new credentials.')

        except KeyError as e:
            log.error(f'Cache file format is invalid: {e}')




    def __str__(self):
        return vars(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


if __name__ == '__main__':
    credential_manager = AWSCredentialsManager(cache_file_path=cfg.cache_file_path)



