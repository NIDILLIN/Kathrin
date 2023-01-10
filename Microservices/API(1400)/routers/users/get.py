import aiohttp
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from config import settings

router = APIRouter()


@router.get('/users')
async def get_all_users():
    """
    {
        'status': 'OK',
        result: {
            'count': int,
            'users': list[User]
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.users+settings.Methods.Users.Get.users    
        ) as resp:
            r = await resp.json()

    return r


@router.get('/users/filter')
async def get_users_with_params(*, skip: int, limit: int):
    """
    {
        'status': 'OK',
        'result': list[User]
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.users+settings.Methods.Users.Get.filter(skip=skip, limit=limit)
        ) as resp:
            r = await resp.json()

    return r

    
@router.get('/users/random')
async def get_random_user():
    """
    {
        'status': 'OK',
        'result': User
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.users+settings.Methods.Users.Get.random
        ) as resp:
            r = await resp.json()
    
    return r


@router.get('/users/{syncId}')
async def get_user(syncId: int):
    """
    {
        'status': 'OK',
        'result': {
            'syncId': int,
            'username': str
            # space: str
            'registration_date': datetime.date (YYYY-MM-DD)
            'wct': Wct (
                'boar_id': str,
                'given_date': datetime.date (YYYY-MM-DD)
            )
            'is_admin': bool
            'premium': bool
            'opened_boars': list[str]
            'jokes': list[str]
            'photos': list[str]
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.users+settings.Methods.Users.Get.user(syncId=syncId)
        ) as resp:
            r = await resp.json()

    return r


@router.get('/users/{syncId}/wct')
async def get_user_wct(syncId: int):
    """
    {
        status: OK,
        result:  Wct (
            'boar_id': str,
            'given_date': datetime.date (YYYY-MM-DD)
        )
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.users+settings.Methods.Users.Get.user_wct(syncId=syncId)
        ) as resp:
            r = await resp.json()
    
    return r


@router.get('/users/{syncId}/avatar')
async def get_avatar(syncId: int):
    return RedirectResponse(settings.users+settings.Methods.Users.Get.avatar(syncId=syncId))
