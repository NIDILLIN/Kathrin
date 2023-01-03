import datetime

from pydantic import BaseModel


class Wct(BaseModel):
    id: str
    given_date: datetime.date


class User(BaseModel):
    syncId: int
    username: str
    registration_date: datetime.date
    wct: Wct | None = None
    is_admin: bool = False
    premium: bool = False
    opened_boars: list[str] | None = None
    jokes: list[str] | None = None
    photos: list[str] | None = None


class NewUser(BaseModel):
    syncId: int
    username: str
    registration_date: datetime.date