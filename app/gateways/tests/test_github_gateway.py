from unittest.mock import Mock
import datetime as dt
from app.gateways.github_gateway import GitHubGatewayImpl
from app.models.github_model import Commits, Repository


def test_get_repositories():
    # Crear una instancia de GitHubGatewayImpl con un mock
    gateway = GitHubGatewayImpl('dummy_access_token', github=Mock())
    gateway.github.get_user().get_repos.return_value = [
        Mock(name='repo1', created_at=dt.datetime(2012, 1, 1), updated_at=dt.datetime(2012, 1, 1))
    ]

    # Llamar al método get_repositories
    repositories = gateway.get_repositories()

    # Comprobar que el resultado sea una lista de objetos Repository
    assert all(isinstance(repo, Repository) for repo in repositories)


def test_get_commits_from_repository():
    # Crear una instancia de GitHubGatewayImpl con un mock
    gateway = GitHubGatewayImpl('dummy_access_token', github=Mock())
    gateway.github.get_user().get_repo("dummy_repo_name").get_commits.return_value = [
        Mock(name='commit1',
             commit=Mock(message='Test commit', author=Mock(name='Author', date='2022-01-01T00:00:00Z')))
    ]

    # Llamar al método get_commits_from_repository
    commits = gateway.get_commits_from_repository('dummy_repo_name')

    # Comprobar que el resultado sea una lista de objetos Commits
    assert all(isinstance(commit, Commits) for commit in commits)
