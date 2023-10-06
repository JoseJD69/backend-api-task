from pydantic import BaseModel


class RepoCommitsRequest(BaseModel):
    repository_name: str
