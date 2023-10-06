import abc

import inject

from app.gateways.github_gateway import GitHubGateway


class ListRepositoriesUseCase(abc.ABC):
    @abc.abstractmethod
    def execute(self) -> dict:
        pass


class ListRepositoriesUseCaseImpl(ListRepositoriesUseCase):
    gateway: GitHubGateway = inject.attr(GitHubGateway)

    def execute(self) -> dict:
        return self.gateway.get_repositories()
