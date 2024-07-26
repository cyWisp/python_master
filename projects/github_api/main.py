import logging
import json

from config import cfg

logging.basicConfig(
    format='%(message)s',
    level=logging.getLevelName(cfg.log_level.upper())
)
log = logging.getLogger()
log.debug(f'Configuration: {json.dumps(vars(cfg), indent=4)}')


if __name__ == '__main__':
    from api.github_api import GithubAPI

    with GithubAPI(cfg.token) as api:
        api.display_repository_information()
        log.info(api.get_commits().totalCount)



