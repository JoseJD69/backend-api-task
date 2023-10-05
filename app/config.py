from pydantic import BaseModel
from app.gateways.github_gateway import GitHubGateway, GitHubGatewayImpl


class Configuration(BaseModel):
    ENVIRONMENT: str
    GITHUB_API_URL: str


def new_configuration():
    configuration = Configuration(ENVIRONMENT="development", GITHUB_API_URL="https://api.github.com")
    return configuration


def di_configuration(binder, configuration=new_configuration()):
    # Gateways
    binder.bind(GitHubGateway, GitHubGatewayImpl(configuration.GITHUB_API_URL))
    # UseCases

