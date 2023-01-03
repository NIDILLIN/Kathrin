import datetime
from fastapi import APIRouter
from fastapi.responses import FileResponse

from db import db

from session import get_session


router = APIRouter()


@router.get('/wct')
async def get_wct_info(syncId: int):
    session = get_session()
    async with session.get(f'http://users:14541/{syncId}/wct/') as resp:
        boar_info = await resp.json()

    today = datetime.date.today().isoformat()

    if today != boar_info.get('given_date'):
        async with session.get(f'http://boars:14545/random') as resp:
            boar = await resp.json()
        await update_user_boar(syncId, boar)
    else:
        boar_id = boar_info['id']
        async with session.get(f'http://boars:14545/{boar_id}') as resp:
            boar = await resp.json()

    return boar


async def update_user_boar(syncId: int, boar):
    session = get_session()
    today = datetime.date.today().isoformat()
    r = {
            'id': boar['id'],
            'given_date': today
        }
    async with session as s:
        await s.put(f'http://users:14541/{syncId}/wct', data=r)


@router.get('/photo')
async def get_photo():
    session = get_session()
    async with session:
        resp = await session.get('photos/random/')

    return resp


@router.get('/joke')
async def get_joke():
    session = get_session()
    async with session:
        resp = await session.get('jokes/random/')

    return resp


@router.get('/boars')
async def get_user_boars(syncId: int):
    session = get_session()
    async with session:
        resp = await session.get(f'achievements/{syncId}/boars/')

    return resp


@router.get('/userstatus')
async def get_user_status(syncId: int):
    session = get_session()
    async with session:
        resp = await session.get(f'users/{syncId}/status')

    return resp




