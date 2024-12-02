import boto3


if __name__ == '__main__':
    sts = boto3.client('sts', p)
    sts.get_caller_identity()