import aiofiles
from fastapi import APIRouter, UploadFile

from db import db
from models import UploadPhoto, Photo, UploadUser

router = APIRouter()


@router.post("/create_photo", response_model=Photo)
async def create_photo(syncId: int, username: str, file: UploadFile):
    uploadUser = UploadUser(
        syncId=syncId,
        username=username
    )
    photo_info = await db.save(uploadUser, file)

    filename = photo_info['filename']
    await save_file(filename, file)

    return {
        'status': 'OK',
        'result': photo_info
    }


async def save_file(filename: str, file: UploadFile):
    async with aiofiles.open('photos/'+filename, 'wb') as f:
        while content := await file.read(1024):
            await f.write(content)
    
    return filename

