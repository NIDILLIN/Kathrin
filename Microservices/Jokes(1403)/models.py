import datetime

from pydantic import BaseModel


class UploadUser(BaseModel):
    syncId: int
    username: str


class UploadJoke(BaseModel):
    text: str
    uploaded_by: UploadUser


class Joke(BaseModel):
    id: str
    text: str
    created_at: datetime.date
    uploaded_by: UploadUser
