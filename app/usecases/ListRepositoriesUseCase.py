import abc
from typing import List

import inject

from app.gateways.github_gateway import GitHubGateway
from app.models.github_model import Repository


class ListRepositoriesUseCase(abc.ABC):
    @abc.abstractmethod
    def execute(self) -> dict:
        pass


class ListRepositoriesUseCaseImpl(ListRepositoriesUseCase):
    gateway: GitHubGateway = inject.attr(GitHubGateway)

    def execute(self) -> List[Repository]:
        return self.gateway.get_repositories()
