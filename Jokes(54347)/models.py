import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    registration_date: datetime.date


class JokePackage(BaseModel):
    joke: str
    date: datetime.date
    uploaded_by: User
