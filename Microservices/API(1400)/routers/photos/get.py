import aiohttp
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from config import settings
from models import Photo, UploadPhoto


router = APIRouter()


@router.get('/photos')
async def get_all_photos():
    """
    {
        'status': OK,
        'result': {
            'count': int,
            'photos': list[Photo]
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.photos+settings.Methods.Photos.Get.photos  
        ) as resp:
            r = await resp.json()

    return r

@router.get('/photos/filter')
async def get_photos_with_params(*, skip: int, limit: int):
    """
    {
        'status': OK,
        'result': list[Photo]
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.photos+settings.Methods.Photos.Get.filter(skip=skip, limit=limit) 
        ) as resp:
            r = await resp.json()

    return r

    
@router.get('/photos/random')
async def get_random_photo():
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
        async with session.get(
            settings.photos+settings.Methods.Photos.Get.random
        ) as resp:
            r = await resp.json()

    return r


@router.get('/photos/{photo_path}')
async def get_file(photo_path: str):
    return RedirectResponse(settings.photos+settings.Methods.Photos.Get.photo(photo_path=photo_path))



