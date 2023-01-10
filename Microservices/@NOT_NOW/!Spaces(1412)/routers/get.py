from datetime import date
from fastapi import APIRouter

from db import db


router = APIRouter()


@router.get('/')
async def get_spaces():
    count, result = await db.get_documents(skip=0, limit=10)
    return {
        'count': count,
        'jokes': result
    }


@router.get('/filter')
async def get_spaces_by_filter(*, skip=0, limit=10):
    ...


@router.get('/{space_name}')
async def get_space(space_name: str):
    space = await db.find(space_name)
    return space


@router.get('/{space_name}/users')
async def get_users_from_space(space_name: str):
    ...


@router.get('/{space_name}/photos')
async def get_users_from_space(space_name: str):
    ...


@router.get('/{space_name}/jokes')
async def get_users_from_space(space_name: str):
    ...


@router.get('/{space_name}/boars')
async def get_users_from_space(space_name: str):
    ...


@router.get('/{space_name}/users/where')
async def get_user_from_space_by_filters(
                            space_name: str,
                            registration_date: date | None = None,
                            is_premium: bool | None = None,
                            is_admin: bool | None = None):
    return {        

    }



