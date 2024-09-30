import logging
import os

import boto3
from botocore.exceptions import ClientError

logging.basicConfig(format='%(message)s', level=logging.INFO)
log = logging.getLogger()
log.name = 'default'

token = '''FwoGZXIvYXdzEFkaDCRb5pT/4LVvgBmbgyLgAWTSZqdFNEdrX0jNWQBJB1upUw0wD0mcLBqx3epls3hBzOSuMjdCUTYtYTSKr64iuZqZ55wo1U4zyPvh0F24Nf/VYIEWQONSZ5OMpbH3CZwPB2J4XZ9OzJP/lsRDF9uL7xBuoPTMuefhlfzYOt8tdzruI75P0zqJuD0P+b5CkaYi6zVa8Xk//wpPOkj/3BcMb3rj3wi+s0bVQVK2ZxhCF+mgflsvXLCst+XjKkyxtjvo6AYFgbnbKeFmRox5r0QwFBxecd0Rqna6V0hLaTfhQEhfJ+jQlEuWF2VdKD+Ab5S/KOzCx7YGMjJsEZwcjQeHbdJP60xDmoKFfPWdb6P30gpBszBo53/FJXpRnUpfKmF5BmzPSe8vKwWpwQ==
'''

def upload_file(
    client: boto3.client,
    file_name: str,
    bucket_name: str,
    object_name: str = None
) -> None:
    """
    Upload a file to an S3 bucket

    :param client: a s3 client object.
    :param file_name: the name of the file to be uploaded.
    :param bucket_name: the target bucket name.
    :param object_name: the name of the object in the target bucket
    :return: None
    """

    new_object_name = None

    # Use base file name if no object name given
    if not object_name:
        new_object_name = f'text/{os.path.basename(file_name)}'
        log.info(object_name)

    # Upload the file
    try:
        log.info(f'Uploading {file_name} to {bucket_name}.')
        client.upload_file(file_name, bucket_name, new_object_name)

        log.info('Upload successful!')

    except ClientError as e:
        logging.error(e)


if __name__ == '__main__':
    s3_client = boto3.client('s3', aws_session_token=token)

    upload_file(
        s3_client,
        'test.txt',
        '853697862182-portal-frontend-landing-dev-docusaurus'
    )


