import datetime

from pydantic import BaseModel


class External(BaseModel):
    type: str
    id: int


class User(BaseModel):
    syncId: int
    telegram: int
    vk: int
    registration_date: datetime.date


class NewUser(BaseModel):
    syncId: int
    registration_date: datetime.date