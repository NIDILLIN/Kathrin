import datetime

from pydantic import BaseModel


class Space(BaseModel):
    # id: str
    name: str
    users: list
    jokes: list
    photos: list
    boars: list

