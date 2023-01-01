from typing import Union
from datetime import date
from pydantic import BaseModel


class FindUser(BaseModel):
    name: Union[str, None]

class UserFriend(BaseModel):
    id: int
    username: str

class WalletStatus:
    OPENED = 'opened'
    CLOSED = 'closed'
    NO_WALLET = 'no_wallet'

class UserWallet(BaseModel):
    status: str
    count: Union[int, None] = None

class UserFriend(BaseModel):
    id: int
    username: str

class UserData(BaseModel):
    opened_boars: list[str]
    jokes: list[str]
    photos_uniq_ids: list[str]
    friends: list[UserFriend]
    is_admin: bool
    premium: bool
    wallet: UserWallet

class User(BaseModel):
    id: int
    username: str
    signedAt: date
    user_data: UserData


class NewUser(BaseModel):
    user_id: int
    username: str
    token: str
    signedAt: date