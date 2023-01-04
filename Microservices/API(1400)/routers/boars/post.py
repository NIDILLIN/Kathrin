import aiofiles
from fastapi import APIRouter, UploadFile

from models import Boar, Category
from config import settings
from session import get_session


router = APIRouter()


@router.post("/boars/create_boar")
async def create_boar(boar: Boar):
    session = get_session()
    async with session.post(
        url=settings.boars+settings.Methods.Boars.Post.create_boar,
        data=boar) as resp:

        r = await resp.json()

    return r


@router.post("/boars/{boar_id}/file")
async def create_upload_file(boar_id: str, file: UploadFile):
    session = get_session()
    async with session.post(
        url=settings.boars+settings.Methods.Boars.Post.create_file(boar_id=boar_id),
        data=file) as resp:

        r = await resp.json()

    return r


@router.post('/boars/categories/create')
async def create_category(category: Category):
    session = get_session()
    async with session.post(
        url=settings.boars+settings.Methods.Boars.Post.create_categoria,
        data=category) as resp:

        r = await resp.json()

    return r