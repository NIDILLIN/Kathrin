from fastapi import APIRouter
from fastapi.responses import FileResponse

from db import db


router = APIRouter()


@router.get('/filter')
async def get_photos_with_params(*, skip: int, limit: int):
    _, result = await db.get_photos(skip=skip, limit=limit)
    return result


@router.get('/')
async def get_all_photos():
    count, result = await db.get_photos(skip=0, limit=10)
    return {
        'count': count,
        'photos': result
    }

    
@router.get('/random')
async def get_random_photo():
    result = await db.random_photo()
    return result


@router.get('/{photo_path}')
async def get_file(photo_path: str):
    return FileResponse(path=f'photos/{photo_path}')



