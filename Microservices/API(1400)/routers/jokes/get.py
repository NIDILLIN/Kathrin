import aiohttp
from fastapi import APIRouter

from config import settings
from models import Joke

router = APIRouter()


@router.get('/jokes')
async def get_all_jokes():
    """
    {
        'status': 'OK',
        'result': {
            'count': int,
            'jokes': list[Joke]
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.jokes+settings.Methods.Jokes.Get.joke
        ) as resp:
            r = await resp.json()

    return r


@router.get('/jokes/filter')
async def get_jokes_with_params(*, skip: int, limit: int):
    """
    {
        'status': 'OK',
        'result': list[Joke]
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.jokes+settings.Methods.Jokes.Get.filter(skip=skip, limit=limit)
        ) as resp:
            r = await resp.json()

    return r


@router.get('/jokes/random', response_model=Joke)
async def get_random_joke():
    """
    {
        'status': 'OK',
        'result': {
            'id': str
            'text': str,
            'created_at': datetime.date (YYYY-MM-DD),
            'uploaded_by': {
                'syncId': int,
                'username': str
            }
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.jokes+settings.Methods.Jokes.Get.random
        ) as resp:
            r = await resp.json()

    return r


@router.get('/jokes/{joke_id}', response_model=Joke)
async def get_joke_by_id(joke_id: str):
    """
    {
        'status': 'OK',
        'result': {
            'id': str
            'text': str,
            'created_at': datetime.date (YYYY-MM-DD),
            'uploaded_by': {
                'syncId': int,
                'username': str
            }
        }
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.jokes+settings.Methods.Jokes.Get.joke(joke_id=joke_id)
        ) as resp:
            r = await resp.json()

    return r




