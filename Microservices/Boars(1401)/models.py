import datetime

from pydantic import BaseModel


class UploadUser(BaseModel):
    syncId: int
    username: str


class Boar(BaseModel):
    id: str
    name: str
    category: str
    premium: bool
    rare: str
    created_at: datetime.date
    created_by: UploadUser


class UploadBoar(BaseModel):
    name: str
    category: str
    premium: bool
    rare: str
    created_by: UploadUser


class UploadCategory(BaseModel):
    name: str


class Category(BaseModel):
    id: str
    name: str
    created_at: datetime.date