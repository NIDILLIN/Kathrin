import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str


class Photo(BaseModel):
    id: str
    name: str
    created_at: datetime.date
    uploaded_by: User
