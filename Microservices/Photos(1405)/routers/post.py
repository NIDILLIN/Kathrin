import aiofiles
from fastapi import APIRouter, UploadFile

from db import db


router = APIRouter()


@router.post("/create_photo")
async def create_upload_file(file: UploadFile):
    id = await save_file(file)
    return {"filename": id+'.png'}


async def save_file(file: UploadFile):
    photo_id = await db.save(file)
    photo_id = str(photo_id)
    async with aiofiles.open('photos/'+photo_id+'.png', 'wb') as f:
        while content := await file.read(1024):
            await f.write(content)
    
    return photo_id

