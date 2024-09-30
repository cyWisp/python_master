import os
import boto3
import sys

from botocore.exceptions import ClientError
from main import log


class S3Manager:
    def __init__(
        self,
        access_key_id: str,
        access_key_secret: str,
        bucket_name: str,
        region_name: str = 'us-east-1',

    ):
        self.region_name, self.bucket_name = region_name, bucket_name

        try:
            log.debug('Authenticating to AWS')
            self.client = boto3.client(
                's3',
                aws_access_key_id=access_key_id,
                aws_secret_access_key=access_key_secret,
            )

        except ClientError as e:
            log.error(f'Authentication failed:\n{e}', exc_info=True)
            sys.exit(1)

    def upload_directory(self, directory_path: str) -> None:
        for file in os.listdir(directory_path):

            log.debug(file)
            file_path = os.path.join(os.path.abspath(directory_path), file)

            try:
                log.info(f'Uploading {file_path}')
                response = self.client.upload_file(file_path, self.bucket_name, file)

                log.info(response)
            except ClientError as e:
                log.error(f'Error uploading {file_path}: {e}', exc_info=True)

    def __str__(self):
        return vars(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            log.debug('Closing s3 client.')
            self.client.close()

        except ClientError as e:
            log.error(f'Error closing s3 client: {e}', exc_info=True)
