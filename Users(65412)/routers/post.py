import aiofiles
from fastapi import APIRouter, UploadFile

from db import db
from models import Boar

router = APIRouter()


@router.post("/boars/file/{boar_id}")
async def create_upload_file(boar_id: str, file: UploadFile):
    id = await save_file(boar_id, file)
    return {
        'status': 'OK',
        "filename": id+'.png'
    }


@router.post("/boars/")
async def create_boar(boar: Boar):
    id = await db.save_documents(boar)
    return {
        'status': 'OK',
        'id': id
    }


async def save_file(boar_id: str, file: UploadFile):
    async with aiofiles.open('boars_photos/'+boar_id+'.png', 'wb') as f:
        while content := await file.read(1024):
            await f.write(content)
    
    return boar_id

