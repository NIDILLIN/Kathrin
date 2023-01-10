import aiohttp
import datetime
from fastapi import APIRouter

from config import settings


router = APIRouter()


@router.get('/wct')
async def get_wct_info(syncId: int):
    """
    {
        'status': 'OK',
        'result': {
            'id': str
            'name': str
            'category': str
            'premium': bool
            'rare': str
            'created_date': datetime.date (YYYY-MM-DD)
            'created_by': {
                'syncId': int,
                'username': str
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.users+settings.Methods.Users.Get.wct(syncId=syncId)
            ) as resp:
                boar_info = await resp.json()

    today = datetime.date.today().strftime('%Y-%m-%d')

    if today != boar_info.get('given_date'):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                settings.boars+settings.Methods.Boars.Get.random
                ) as resp:
                rand_boar = await resp.json()
        await update_user_boar(syncId, rand_boar)
    else:
        boar_id = boar_info['boar_id']
        async with aiohttp.ClientSession() as session:
            async with session.get(
                settings.boars+settings.Methods.Boars.Get.boar(boar_id=boar_id)
            ) as resp:
                boar = await resp.json()

    return boar


async def update_user_boar(syncId: int, boar):
    today = datetime.date.today().strftime('%Y-%m-%d')
    r = {
            'id': boar['boar_id'],
            'given_date': today
        }
    async with aiohttp.ClientSession() as session:
        async with session.patch(
            settings.users+settings.Methods.Users.Patch.user_wct(syncId=syncId),
            json=r
            ) as resp:
                res = await resp.json()


@router.get('/photo')
async def get_photo():
    """
    {
        'status': 'OK',
        'result': {
            'id': str,
            'filename': str,
            'created_at': datetime.date (YYYY-MM-DD)
            'uploaded_by': {
                'syncId': int,
                'username': str
            }
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get('photos/random/') as resp:
            result = await resp.json()

    return result


@router.get('/joke')
async def get_joke():
    """
    {
        'status': 'OK',
        'result': {
            'id': str
            'text': str,
            'created_at': datetime.date (YYYY-MM-DD),
            'uploaded_by': {
                'syncId': int,
                'username': str
            }
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get('jokes/random/') as resp:
            result = await resp.json()

    return result


@router.get('/boars')
async def get_user_boars(syncId: int):
    """
    {
        'status': 'OK',
        'result': list[Boar]
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(f'achievements/{syncId}/boars/') as resp:
            result = await resp.json()

    return result


@router.get('/userstatus')
async def get_user_status(syncId: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'users/{syncId}/status') as resp:
            result = await resp.json()

    return result




