import aiofiles
from fastapi import APIRouter, UploadFile

from db import db
from models import NewUser

router = APIRouter()


@router.post("/{syncId}/avatar")
async def create_user_avatar(syncId: int, file: UploadFile):
    id = await save_file(syncId, file)
    await db.save_avatar(syncId)
    return {
        'status': 'OK',
        "filename": id+'.png'
    }


@router.post("/new_user")
async def create_new_user(newUser: NewUser):
    user = await db.create_user(newUser)
    return user


async def save_file(syncId: str, file: UploadFile):
    async with aiofiles.open('avatars/'+syncId+'.png', 'wb') as f:
        while content := await file.read(1024):
            await f.write(content)
    
    return syncId

