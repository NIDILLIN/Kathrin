from fastapi import APIRouter

from config import settings


router = APIRouter()


@router.get('/jokes/')
async def get_jokes(skip=0, limit=10):
    ...


@router.get('/jokes')
async def get_jokes_with_params(*, start: int, limit: int):
    ...


@router.get('/jokes/random')
async def get_random_joke():
    ...
