import abc


class GitHubGateway(abc.ABC):

    @abc.abstractmethod
    def get_repositories(self) -> dict:
        pass

    def get_commits_from_repository(self, repo_name: str) -> dict:
        pass


class GitHubGatewayImpl(GitHubGateway):

    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_repositories(self) -> dict:
        pass

    def get_commits_from_repository(self, repo_name: str) -> dict:
        pass
