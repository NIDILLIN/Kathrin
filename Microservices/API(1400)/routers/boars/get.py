import aiohttp
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from config import settings


router = APIRouter()


@router.get('/boars')
async def get_all_boars():
    """
    {
        'status': 'OK',
        'result': {
            'count': int,
            'boars': list[Boar]
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.boars+settings.Methods.Boars.Get.boars
        ) as resp:
            r = await resp.json()

    return r


@router.get('/boars/filter')
async def get_boars_with_params(*, skip: int, limit: int):
    """
    {
        'status': 'OK',
        'result': list[Boar]
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.boars+settings.Methods.Boars.Get.filter(skip=skip, limit=limit)
        ) as resp:
            r = await resp.json()

    return r

    
@router.get('/boars/random')
async def get_random_boar():
    """
    {
        'status': 'OK',
        'result': {
            'id': str
            'name': str
            'category': str
            'premium': bool
            'rare': str
            'created_date': datetime.date (YYYY-MM-DD)
            'created_by': {
                'syncId': int,
                'username': str
        }
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.boars+settings.Methods.Boars.Get.random
        ) as resp:
            r = await resp.json()

    return r


@router.get('/boars/{boar_id}')
async def get_boar(boar_id: str):
    """
    {
        'status': 'OK',
        'result': {
            'id': str
            'name': str
            'category': str
            'premium': bool
            'rare': str
            'created_date': datetime.date (YYYY-MM-DD)
            'created_by': {
                'syncId': int,
                'username': str
        }
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.boars+settings.Methods.Boars.Get.boar(boar_id=boar_id)
        ) as resp:
            r = await resp.json()

    return r


@router.get('/boars/{boar_id}/file')
async def get_file(boar_id: str):
    return RedirectResponse(settings.boars+settings.Methods.Boars.Get.file(boar_id=boar_id))


@router.get('/boars/categories')
async def get_all_categories():
    """
    {
        'status': 'OK',
        'result': {
            'count': int,
            'categories': list[Category]
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.boars+settings.Methods.Boars.Get.categories
        ) as resp:
            r = await resp.json()

    return r


@router.get('/boars/categories/{category_id}')
async def get_all_boars_of_category(category_id: str):
    """
    {
        'status': 'OK',
        'result': {
            'id': str,
            'name': str,
            'created_date': datetime.date (YYYY-MM-DD)
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.boars+settings.Methods.Boars.Get.category(category_id=category_id)
        ) as resp:
            r = await resp.json()

    return r

