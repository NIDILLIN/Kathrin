from fastapi import APIRouter
from fastapi.responses import FileResponse, RedirectResponse

from config import settings
from session import get_session

router = APIRouter()


@router.get('/users')
async def get_all_users():
    session = get_session()
    async with session.get(
        settings.users+settings.Methods.Users.Get.users) as resp:

        r = await resp.json()

    return r


@router.get('/users/filter')
async def get_users_with_params(*, skip: int, limit: int):
    session = get_session()
    async with session.get(
        settings.users+settings.Methods.Users.Get.filter(skip=skip, limit=limit)) as resp:

        r = await resp.json()

    return r

    
@router.get('/users/random')
async def get_random_user():
    session = get_session()
    async with session.get(
        settings.users+settings.Methods.Users.Get.random) as resp:

        r = await resp.json()

    return r


@router.get('/users/{syncId}')
async def get_user(syncId: int):
    session = get_session()
    async with session.get(
        settings.users+settings.Methods.Users.Get.user(syncId=syncId)) as resp:

        r = await resp.json()

    return r


@router.get('/users/{syncId}/wct')
async def get_user_wct(syncId: int):
    session = get_session()
    async with session.get(
        settings.users+settings.Methods.Users.Get.user_wct(syncId=syncId)) as resp:

        r = await resp.json()

    return r


@router.get('/users/{syncId}/avatar')
async def get_avatar(syncId: int):
    return RedirectResponse(settings.users+settings.Methods.Users.Get.avatar(syncId=syncId))
