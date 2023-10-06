import abc
from typing import List

from github import Github
from github import Auth


class GitHubGateway(abc.ABC):

    @abc.abstractmethod
    def get_repositories(self) -> dict:
        pass

    def get_commits_from_repository(self, repo_name: str) -> dict:
        pass


class GitHubGatewayImpl(GitHubGateway):

    def __init__(self, access_token: str):
        auth = Auth.Token(access_token)
        self.github = Github(auth=auth)

    def get_repositories(self) -> List[dict]:
        repos = self.github.get_user().get_repos()
        print(repos)
        return [{"name": repo.name, "url": repo.url} for repo in repos]

    def get_commits_from_repository(self, repo_name: str) -> dict:
        pass
