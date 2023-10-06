import datetime as dt

from pydantic import BaseModel


class Repository(BaseModel):
    name: str
    created_at: dt.datetime
    updated_at: dt.datetime


class Commits(BaseModel):
    message: str
    author: str
    created_at: dt.datetime
