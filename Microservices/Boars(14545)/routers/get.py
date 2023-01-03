from fastapi import APIRouter
from fastapi.responses import FileResponse

from db import db


router = APIRouter()


@router.get('/')
async def get_all_boars():
    count, result = await db.get_documents(skip=0, limit=10)
    return {
        'status': 'OK',
        'result': {
            'count': count,
            'boars': result
        }
    }


@router.get('/filter')
async def get_boars_with_params(*, skip: int, limit: int):
    _, result = await db.get_documents(skip=skip, limit=limit)
    return result

    
@router.get('/random')
async def get_random_boar():
    result = await db.random_document()
    return result


@router.get('/{boar_id}')
async def get_boar(boar_id: str):
    boar = await db.find(boar_id)
    return boar


@router.get('/{boar_id}/file')
async def get_file(boar_id: str):
    return FileResponse(path=f'boars_photos/{boar_id}.png')


@router.get('/categories')
async def get_all_categories():
    count, categories = await db.get_categories()
    return {
        'count': count,
        'categories': categories
    }




