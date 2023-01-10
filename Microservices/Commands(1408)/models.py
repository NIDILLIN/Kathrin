from typing import Union
import datetime

from pydantic import BaseModel

class Wct(BaseModel):
    boar_id: str
    given_date: datetime.date

    
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


class Boar(BaseModel):
    id: str
    name: str
    category: str
    premium: bool
    rare: str
    created_at: datetime.date
    created_by: User


class Photo(BaseModel):
    id: str
    filename: str
    created_at: datetime.date
    uploaded_by: UploadUser
