import aiohttp
from fastapi import APIRouter, UploadFile

from models import UploadBoar, UploadCategory
from config import settings


router = APIRouter()


@router.post("/boars/create_boar")
async def create_boar(boar: UploadBoar):
    """
    {
        'status': 'OK',
        'result': {
            'name': str
            'category': str
            'premium': bool
            'rare': str
            'created_at': datetime.date (YYYY-MM-DD)
            'created_by': {
                'syncId': int,
                'username': str
            }
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(
            settings.boars+settings.Methods.Boars.Post.create_boar,
            json=boar.dict()    
        ) as resp:
            r = await resp.json()

    return r


@router.post("/boars/{boar_id}/file")
async def create_upload_file(boar_id: str, file: UploadFile):
    """
    {
        'status': 'OK',
        'filename': str
    }
    """
    file_bytes = await file.read()
    async with aiohttp.ClientSession() as session:
        async with session.post(
            settings.boars+settings.Methods.Boars.Post.create_file(boar_id=boar_id),
            data=file_bytes    
        ) as resp:
            r = await resp.json()

    return r


@router.post('/boars/categories/create')
async def create_category(category: UploadCategory):
    """
    {
        'status': 'OK',
        'result': {
            'id': str,
            'name': str, 
            'created_at': datetime.date (YYYY-MM-DD)
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(
            settings.boars+settings.Methods.Boars.Post.create_categoria,
            json=category.dict()
        ) as resp:
            r = await resp.json()

    return r