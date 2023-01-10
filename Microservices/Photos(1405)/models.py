import datetime

from pydantic import BaseModel


class UploadUser(BaseModel):
    syncId: int
    username: str


class UploadPhoto(BaseModel):
    name: str
    uploaded_by: UploadUser


class Photo(BaseModel):
    id: str
    filename: str
    created_at: datetime.date
    uploaded_by: UploadUser
