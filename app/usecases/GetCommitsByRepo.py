import abc
from typing import List

import inject

from app.gateways.github_gateway import GitHubGateway


class GetCommitsByRepoUseCase(abc.ABC):
    @abc.abstractmethod
    def execute(self, repo_name: str) -> dict:
        pass


class GetCommitsByRepoUseCaseImpl(GetCommitsByRepoUseCase):
    gateway: GitHubGateway = inject.attr(GitHubGateway)

    def execute(self, repo_name: str) -> List[dict]:
        return self.gateway.get_commits_from_repository(repo_name)
