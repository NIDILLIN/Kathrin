from fastapi import APIRouter
from fastapi.responses import FileResponse, RedirectResponse

from config import settings
from session import get_session


router = APIRouter()


@router.get('/boars')
async def get_all_boars():
    session = get_session()
    async with session.get(
        settings.boars+settings.Methods.Boars.Get.boars) as resp:

        r = await resp.json()

    return r


@router.get('/boars/filter')
async def get_boars_with_params(*, skip: int, limit: int):
    session = get_session()
    async with session.get(
        settings.boars+settings.Methods.Boars.Get.filter(skip=skip, limit=limit)) as resp:

        r = await resp.json()

    return r

    
@router.get('/boars/random')
async def get_random_boar():
    session = get_session()
    async with session.get(
        settings.boars+settings.Methods.Boars.Get.random) as resp:

        r = await resp.json()

    return r


@router.get('/boars/{boar_id}')
async def get_boar(boar_id: str):
    session = get_session()
    async with session.get(
        settings.boars+settings.Methods.Boars.Get.boar(boar_id=boar_id)) as resp:

        r = await resp.json()

    return r


@router.get('/boars/{boar_id}/file')
async def get_file(boar_id: str):
    return RedirectResponse(settings.boars+settings.Methods.Boars.Get.file(boar_id=boar_id))


@router.get('/boars/categories')
async def get_all_categories():
    session = get_session()
    async with session.get(
        settings.boars+settings.Methods.Boars.Get.categories) as resp:

        r = await resp.json()

    return r



