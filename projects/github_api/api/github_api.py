from github import Github, Auth
from main import log


class GithubAPI:
    def __init__(
        self,
        token: str = None,
    ):
        self.github_client = self.authenticate(token)

    def __str__(self):
        return vars(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.github_client.close()

    @staticmethod
    def authenticate(token):
        try:
            log.info('Authenticating.')

            github_auth = Auth.Token(token)
            return Github(auth=github_auth)

        except Exception as e:
            log.error(f'Something went wrong: {e}.')

    def display_repository_information(self):
        try:
            log.info('Getting a list of all repositories.')

            for repo in self.github_client.get_user().get_repos():
                log.info(repo.name)

        except Exception as e:
            log.error(f'Something went wrong: {e}.')

    def get_releases(self, repo_name):
        repo = self.github_client.get_repo(repo_name)
        return repo.get_releases()

