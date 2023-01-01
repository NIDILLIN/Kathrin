from fastapi import APIRouter
from fastapi.responses import FileResponse

from db import db


router = APIRouter()


@router.get('/boars')
async def get_boars_with_params(*, skip: int, limit: int):
    _, result = await db.get_documents(skip=skip, limit=limit)
    return result


@router.get('/boars/')
async def get_all_boars():
    count, result = await db.get_documents(skip=0, limit=10)
    return {
        'count': count,
        'boars': result
    }

    
@router.get('/boars/random', response_model=str)
async def get_random_boar():
    result = await db.random_document()
    return result


@router.get('/boar/{boar_id}')
async def get_boar(boar_id: str):
    boar = await db.find(boar_id)
    return {
        'status': 'OK',
        'result': boar
    }


@router.get('/boar/file/{boar_path}')
async def get_file(photo_path: str):
    return FileResponse(path=f'photos/{photo_path}')



