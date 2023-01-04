import datetime
from pydantic import BaseModel

class Wct(BaseModel):
    id: str
    given_date: datetime.date


class NewUser(BaseModel):
    syncId: int
    username: str
    registration_date: datetime.date


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


class UploadUser(BaseModel):
    syncId: int
    username: str


class Photo(BaseModel):
    id: str
    name: str
    created_at: datetime.date
    uploaded_by: UploadUser


class Joke(BaseModel):
    joke: str
    created_by: UploadUser


class JokePackage(BaseModel):
    id: str
    joke: str
    created_at: datetime.date
    created_by: UploadUser


class ChatGPTMessage(BaseModel):
    model: str
    prompt: str
    temperature: float
    max_tokens: int
    top_p: float
    frequency_penalty: float
    presence_penalty: float


class Boar(BaseModel):
    # id: str
    name: str
    category: str
    premium: bool
    rare: str
    created_at: datetime.date
    created_by: User


class Category(BaseModel):
    category: str
    created_at: datetime.date