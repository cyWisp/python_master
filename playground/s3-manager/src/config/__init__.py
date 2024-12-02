import configargparse
import dotenv


dotenv.load_dotenv()

parser = configargparse.get_argument_parser(
    description='AWS S3 Management Configuration',
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter,
)

parser.add_argument(
    '-l',
    '--log-level',
    type=str,
    required=False,
    default='info',
    env_var='LOG_LEVEL',
    help='Log level',
)

parser.add_argument(
    '-i',
    '--access-key-id',
    type=str,
    required=True,
    env_var='AWS_ACCESS_KEY_ID',
    help='AWS Access Key ID',
)

parser.add_argument(
    '-k',
    '--secret-access-key',
    type=str,
    required=True,
    env_var='AWS_SECRET_ACCESS_KEY',
    help='AWS Secret Access Key',
)

parser.add_argument(
    '-r',
    '--region',
    type=str,
    required=False,
    env_var='REGION',
    default='us-east-1',
    help='AWS Region',
)

parser.add_argument(
    '-b',
    '--bucket-name',
    type=str,
    required=True,
    env_var='BUCKET_NAME',
    help='AWS S3 Bucket',
)

parser.add_argument(
    '-t',
    '--target-directory',
    type=str,
    required=True,
    env_var='TARGET_DIRECTORY',
    help='Target directory',
)

cfg = parser.parse_known_args()[0]
