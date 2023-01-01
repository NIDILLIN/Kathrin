import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    token: str
    registration_date: datetime.date

