import datetime

from typing import Union
from fastapi import APIRouter

from config import settings

from models import User, UserData, UserWallet, WalletStatus


router = APIRouter()


@router.get('/users/where')
async def get_user_by_filters(*,
                            name: str,
                            signedAt: Union[datetime.date, None],
                            is_premium: Union[bool, None],
                            is_admin: Union[bool, None]):
    return {        

    }


@router.get('/users/{user_id}', response_model=User)
async def get_user(user_id: int):
    user = await find_user(user_id)

    return user


@router.get('/users/{user_id}/wct')
async def get_user_wct(user_id: int):
    ...


async def find_user(user_id: int):
    user = User(
        id=user_id,
        username='',
        signedAt='',
        user_data=UserData(
            opened_boars=[],
            jokes=[],
            photos_uniq_ids=[],
            friends=[],
            is_admin=False,
            premium=False,
            wallet=UserWallet(status=WalletStatus.NO_WALLET)
        )
    )
    return user