import logging
from config import cfg

logging.basicConfig(
    format='%(process)d - %(asctime)s - %(filename)s - '
           '%(funcName)s - %(levelname)s: %(message)s',
    level=logging.getLevelName(cfg.log_level.upper())
)
log = logging.getLogger()


if __name__ == '__main__':
    from api.api import S3Manager

    with S3Manager(
        cfg.access_key_id,
        cfg.secret_access_key,
        cfg.bucket_name,
    ) as s3:
        s3.upload_directory(cfg.target_directory)


