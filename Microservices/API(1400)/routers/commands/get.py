import aiohttp
from fastapi import APIRouter

from config import settings


router = APIRouter()


@router.get('/commands/wct')
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
            settings.commands+settings.Methods.Commands.Get.wct(syncId=syncId)    
        ) as resp:
            r = await resp.json()

    return r


@router.get('/commands/photo')
async def get_photo():
    photo_info = await session.get(
        settings.commands+settings.Methods.Commands.Get.photo
    )

    return photo_info


@router.get('/commands/joke')
async def get_joke():
    joke = await session.get(
        settings.commands+settings.Methods.Commands.Get.joke
    )

    return joke


@router.get('/commands/boars')
async def get_user_boars(syncId: int):
    boars = await session.get(
        settings.commands+settings.Methods.Commands.Get.boars(syncId=syncId)
    )

    return boars


# @router.get('/commands/userstatus')
# async def get_user_status(syncId: int):
#     session = get_session()
#     async with session:
#         resp = await session.get(f'users/{syncId}/status')

#     return resp




