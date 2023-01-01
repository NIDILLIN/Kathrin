import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    date: datetime.date


# class Photo(BaseModel):
#     uploaded_by: User

class Photo(BaseModel):
    id: str
    name: str
