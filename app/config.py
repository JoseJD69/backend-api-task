from pydantic import BaseModel
from app.gateways.github_gateway import GitHubGateway, GitHubGatewayImpl
from decouple import config

from app.usecases.ListRepositoriesUseCase import ListRepositoriesUseCase, ListRepositoriesUseCaseImpl


class Configuration(BaseModel):
    ENVIRONMENT: str
    GITHUB_TOKEN: str


def new_configuration():
    configuration = Configuration(ENVIRONMENT=config("ENVIRONMENT"), GITHUB_TOKEN=config("GITHUB_TOKEN"))
    return configuration


def di_configuration(binder, configuration=new_configuration()):
    # Gateways
    binder.bind(GitHubGateway, GitHubGatewayImpl(configuration.GITHUB_TOKEN))
    # UseCases
    binder.bind(ListRepositoriesUseCase, ListRepositoriesUseCaseImpl())
