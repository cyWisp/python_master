import asyncio
from github import Github, Auth
from github.GithubException import GithubException
from main import log


class GithubAPI:
    def __init__(
        self,
        token: str = None,
        repository_name: str = None
    ):
        self.github_client = self._authenticate(token)
        self.total_available_release_pages = 10000 // 30
        self.releases = self._get_all_releases(repository_name)

        self.release_page_queue = asyncio.Queue()

    @staticmethod
    def _authenticate(token):
        try:
            log.info('Authenticating.')

            github_auth = Auth.Token(token)
            return Github(auth=github_auth)

        except Exception as e:
            log.error(f'Something went wrong: {e}.')

    # Releases
    def _get_all_releases(self, repo_name: str):
        try:
            log.info(f'Gathering releases for repository {repo_name}.')

            repo = self.github_client.get_repo(repo_name)
            return repo.get_releases()

        except GithubException as e:
            log.error(f'Exceeded maximum available results (10,000).\n{e}')

    async def _get_release_items(self):
        count = 0

        while True:
            try:
                log.info(f'Getting all releases in page {count}.')
                page = self.releases.get_page(count)

                for release in page:
                    log.info(f'Adding {release.id} | {release.title} to queue.')
                    await self.release_page_queue.put({
                        'id': release.id,
                        'title': release.title,
                        'published_at': release.published_at,
                        'is_draft': release.draft
                    })

                count += 1
                await asyncio.sleep(.5)

            except GithubException as e:
                log.error(f'Exceeded maximum available results.\n{e}')
                asyncio.current_task().cancel()

    async def _delete_release(self, release_object: dict) -> None:
        try:
            if release_object['published_at'] is None and release_object['is_draft']:
                log.info(f'Deleting {release_object["id"]}.')
                # TODO: delete release

        except GithubException as e:
            log.error(e)

    async def _process_release_items(self):
        while True:
            try:
                current_item = await self.release_page_queue.get()
                log.info(f'Processing release item {current_item}.')

                log.debug(f'Id: {current_item["id"]} | Title: {current_item["title"]} | '
                          f'Published: {current_item["published_at"]} | Is Draft: {current_item["is_draft"]}')

                await self._delete_release(current_item)
                self.release_page_queue.task_done()

            except asyncio.exceptions.CancelledError:
                raise

    async def delete_release_dry_run(self):
        try:
            log.info('Building and running tasks.')

            build_queue_task = asyncio.create_task(self._get_release_items())
            process_queue_task = asyncio.create_task(self._process_release_items())

            await asyncio.gather(build_queue_task, process_queue_task)
            await self.release_page_queue.join()

        except asyncio.CancelledError:
            return

    def __str__(self):
        return vars(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.github_client.close()
