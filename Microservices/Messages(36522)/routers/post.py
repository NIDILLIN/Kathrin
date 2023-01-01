import aiofiles
from fastapi import APIRouter, UploadFile

from models import Message
from db import db


router = APIRouter()


@router.post("/messages/")
async def create_message(message: Message):
    id = await db.save(message)
    return {
        'status': 'OK',
        'message_id': id
    }



@router.post("/messages/{message_id}/file")
async def create_message_file(message_id: str, file: UploadFile):
    id = await save_file(message_id, file)
    return {
        "status": "OK",
        "filename": id+'.png'
    }


async def save_file(message_id: str, file: UploadFile):
    async with aiofiles.open('photos/'+message_id+'.png', 'wb') as f:
        while content := await file.read(1024):
            await f.write(content)
    
    return message_id