from fastapi import APIRouter
from fastapi.responses import FileResponse

from db import db

from session import get_session


router = APIRouter()


@router.get('/wct')
async def get_wct_info(syncId: int):
    session = get_session()
    async with session:
        boar_info = await session.get(f'users/{syncId}/wct/')

    return boar_info


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


@router.get('/auth')
async def get_photos_with_params():
    ...


@router.get('/boars')
async def get_user_boars(syncId: int):
    session = get_session()
    async with session:
        resp = await session.get(f'users/{syncId}/boars/')

    return resp


@router.get('/help')
async def get_photos_with_params():
    ...


@router.get('/userstatus')
async def get_user_status(syncId: int):
    session = get_session()
    async with session:
        resp = await session.get(f'users/{syncId}/status')

    return resp




