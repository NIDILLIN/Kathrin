import datetime
from typing import Union
from fastapi import APIRouter

from config import settings
from session import get_session
from models import NewUser


router = APIRouter()


@router.get('/spaces/{space_name}')
async def get_root(space_name: str):
    ...


@router.get('/spaces/{space_name}/users')
async def get_users_from_space(space_name: str):
    ...


@router.get('/spaces/{space_name}/users/where')
async def get_user_from_space_by_filters(space_name: str,
                            name: str,
                            signedAt: Union[datetime.date, None],
                            is_premium: Union[bool, None],
                            is_admin: Union[bool, None]):
    return {        

    }