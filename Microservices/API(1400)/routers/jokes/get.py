from fastapi import APIRouter

from config import settings
from session import get_session


router = APIRouter()


@router.get('/jokes')
async def get_all_jokes():
    session = get_session()
    async with session.get(
        settings.jokes+settings.Methods.Jokes.Get.jokes) as resp:

        r = await resp.json()

    return r


@router.get('/jokes/filter', response_model=list[str])
async def get_jokes_with_params(*, skip: int, limit: int):
    session = get_session()
    async with session.get(
        settings.jokes+settings.Methods.Jokes.Get.filter) as resp:

        r = await resp.json()

    return r


@router.get('/jokes/random')
async def get_random_joke():
    session = get_session()
    async with session.get(
        settings.jokes+settings.Methods.Jokes.Get.random) as resp:

        r = await resp.json()

    return r


@router.get('/jokes/{joke_id}')
async def get_joke_by_id(joke_id: str):
    session = get_session()
    async with session.get(
        settings.jokes+settings.Methods.Jokes.Get.joke(joke_id=joke_id)) as resp:

        r = await resp.json()

    return r




