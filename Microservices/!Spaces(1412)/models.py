import datetime

from pydantic import BaseModel


class JokePackage(BaseModel):
    joke: str
    date: datetime.date
