import aiohttp
from fastapi import APIRouter

from config import settings


router = APIRouter()


def get_session():
    return aiohttp.ClientSession()


@router.get('/photos/')
async def get_photos():
    async with aiohttp.ClientSession() as session:
        async with session.get(settings.photos_api) as response:
            return response


@router.get('/photos')
async def get_photos_with_params(*, skip: int, limit: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(settings.photos_api, params=dict(skip=skip, limit=limit)) as response:
            return response


@router.get('/photos/random')
async def get_random_photo():
    ...


@router.get('/photos/{photo_id}')
async def get_photo(photo_id: int):
    ...