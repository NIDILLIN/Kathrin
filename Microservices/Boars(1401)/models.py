import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    registration_date: datetime.date


class Boar(BaseModel):
    # id: str
    name: str
    category: str
    premium: bool
    rare: str
    created_date: datetime.date
    created_by: User


class Category(BaseModel):
    category: str
    created_at: datetime.date