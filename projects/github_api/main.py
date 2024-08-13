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
        # api.display_repository_information()
        # log.info(api.get_commits().totalCount)
        releases = api.get_releases('ccsq-qdas/portal')

        count = 0
        pages = []

        page = releases.get_page(200)
        for release in page:
            log.info(f'{release.title} | {release.published_at}')

        # while True:
        #     try:
        #         page = releases.get_page(count)
        #
        #         if not page:
        #             raise IndexError
        #
        #         for release in page:
        #             log.info(f'{release.title} | {release.published_at}')
        #
        #         count += 1
        #
        #     except IndexError:
        #         break
        #
        # log.info(len(pages))








