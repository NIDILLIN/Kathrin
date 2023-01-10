import datetime
from typing import Union

from pydantic import BaseModel


class Wct(BaseModel):
    boar_id: str
    given_date: datetime.date


class User(BaseModel):
    syncId: int
    username: str
    registration_date: datetime.date
    wct: Union[Wct, None] = None
    is_admin: bool = False
    premium: bool = False
    opened_boars: Union[list[str], None] = None
    jokes: Union[list[str], None] = None
    photos: Union[list[str], None] = None


class NewUser(BaseModel):
    syncId: int
    username: str
    registration_date: datetime.date