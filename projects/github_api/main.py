import logging
import json
import asyncio

from config import cfg

logging.basicConfig(
    format='%(process)d - %(asctime)s - %(filename)s - %(funcName)s - %(levelname)s: %(message)s',
    level=logging.getLevelName(cfg.log_level.upper())
)
log = logging.getLogger()
log.debug(f'Configuration: {json.dumps(vars(cfg), indent=4)}')


if __name__ == '__main__':
    from api.github_api import GithubAPI

    with GithubAPI(cfg.token, repository_name='ccsq-qdas/portal') as api:
        log.info(api.releases)
        asyncio.run(api.delete_release_dry_run())

        # log.info(f'{dir(releases)}\n{releases.totalCount}')
        #
        # time.sleep(5)
        # page = releases.get_page(1)
        # log.info(len(page))

        # for release in page:
        #     log.info(f'{release.title} | {release.published_at} | {release.draft}')
        #     log.info(dir(release))










