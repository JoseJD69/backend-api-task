from pydantic import BaseModel


class Configuration(BaseModel):
    ENVIRONMENT: str
    GITHUB_API_URL: str


def new_configuration():
    configuration = Configuration(ENVIRONMENT="development", GITHUB_API_URL="https://api.github.com")
    return configuration


def di_configuration(binder, configuration=new_configuration()):
    # UseCases
    pass
