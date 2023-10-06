import abc
from typing import List

from github import Github
from github import Auth

from app.models.github_model import Repository, Commits


class GitHubGateway(abc.ABC):

    @abc.abstractmethod
    def get_repositories(self) -> List[Repository]:
        pass

    def get_commits_from_repository(self, repo_name: str) -> List[Commits]:
        pass


class GitHubGatewayImpl(GitHubGateway):

    def __init__(self, access_token: str, github: Github = None):
        auth = Auth.Token(access_token)
        self.github = github or Github(auth=auth)

    def get_repositories(self) -> List[Repository]:
        repos = self.github.get_user().get_repos()
        return [Repository(name=str(repo.name), created_at=repo.created_at,
                           updated_at=repo.updated_at) for repo in repos]

    def get_commits_from_repository(self, repo_name: str) -> List[Commits]:
        commits = self.github.get_user().get_repo(repo_name).get_commits()
        return [Commits(message=commit.commit.message, author=str(commit.commit.author.name),
                        created_at=commit.commit.author.date) for commit in commits]
