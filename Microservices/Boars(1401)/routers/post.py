import aiofiles
from fastapi import APIRouter, UploadFile

from db import db
from models import Boar, Category

router = APIRouter()


@router.post("/create_boar")
async def create_boar(boar: Boar):
    id = await db.save_document(boar)
    return {
        'status': 'OK',
        'id': id
    }


@router.post("/{boar_id}/file")
async def create_upload_file(boar_id: str, file: UploadFile):
    id = await save_file(boar_id, file)
    return {
        'status': 'OK',
        "filename": id+'.png'
    }


async def save_file(boar_id: str, file: UploadFile):
    async with aiofiles.open('boars_photos/'+boar_id+'.png', 'wb') as f:
        while content := await file.read(1024):
            await f.write(content)
    
    return boar_id


@router.post('/categories/create')
async def create_category(category: Category):
    await db.save_category(category)
    return {
        'status': 'OK'
    }
