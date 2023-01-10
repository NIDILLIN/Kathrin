import aiofiles
from fastapi import APIRouter, UploadFile

from db import db
from models import UploadBoar, UploadCategory, Boar

router = APIRouter()


@router.post("/create_boar")
async def create_boar(uploadBoar: UploadBoar):
    boar = await db.save_document(uploadBoar)
    return {
        'status': 'OK',
        'result': boar
    }


@router.post("/{boar_id}/file")
async def create_upload_file(boar_id: str, file: UploadFile):
    id = await save_file(boar_id, file)
    filename = id+'.png'
    return {
        'status': 'OK',
        'filename': filename
    }


async def save_file(boar_id: str, file: UploadFile):
    async with aiofiles.open('boars_photos/'+boar_id+'.png', 'wb') as f:
        while content := await file.read(1024):
            await f.write(content)
    
    return boar_id


@router.post('/categories/create')
async def create_category(uploadCategory: UploadCategory):
    category = await db.save_category(uploadCategory)
    return {
        'status': 'OK',
        'result': category
    }
