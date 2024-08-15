import asyncio
import json
import logging

from config import cfg

logging.basicConfig(
    format='%(process)d - %(asctime)s - %(filename)s - '
           '%(funcName)s - %(levelname)s: %(message)s',
    level=logging.getLevelName(cfg.log_level.upper())
)
log = logging.getLogger()


if __name__ == '__main__':
    log.debug(f'Configuration: {json.dumps(vars(cfg), indent=4)}')

    from api.github_api import GithubAPI

    with GithubAPI(
        cfg.token,
        repository_name=cfg.repository_name,
        dry_run=(cfg.dry_run.title() == 'True')
    ) as api:
        # log.info(api.releases)
        # asyncio.run(api.delete_release_dry_run())

        log.info('Testing.')
        log.info(api.__str__())
