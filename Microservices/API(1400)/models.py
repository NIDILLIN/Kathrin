import datetime
from typing import Union
from pydantic import BaseModel


class External(BaseModel):
    type: str
    id: int


class Wct(BaseModel):
    boar_id: str
    given_date: datetime.date


class NewUser(BaseModel):
    syncId: int
    username: str
    registration_date: datetime.date


class User(BaseModel):
    syncId: int
    username: str
    # space: str
    registration_date: datetime.date
    wct: Union[ Wct, None] = None
    is_admin: bool = False
    premium: bool = False
    opened_boars: Union[list[str], None] = None
    jokes: Union[list[str], None] = None
    photos: Union[list[str], None] = None


class UploadUser(BaseModel):
    syncId: int
    username: str


class Photo(BaseModel):
    id: str
    filename: str
    created_at: datetime.date
    uploaded_by: UploadUser


class UploadJoke(BaseModel):
    text: str
    uploaded_by: UploadUser


class Joke(BaseModel):
    id: str
    text: str
    created_at: datetime.date
    uploaded_by: UploadUser


class ChatGPTMessage(BaseModel):
    model: str
    prompt: str
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float


class Boar(BaseModel):
    id: str
    name: str
    category: str
    premium: bool
    rare: str
    created_at: datetime.date
    created_by: User


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