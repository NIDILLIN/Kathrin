from fastapi import APIRouter

from db import db
from models import Joke

router = APIRouter()


@router.get('/filter')
async def get_jokes_with_params(*, skip: int, limit: int):
    _, result = await db.get_documents(skip=skip, limit=limit)
    return {
        'status': 'OK',
        'result': result
    }


@router.get('/')
async def get_all_jokes():
    count, result = await db.get_documents(skip=0, limit=10)
    return {
        'status': 'OK',
        'result': {
            'count': count,
            'jokes': result
        }
    }


@router.get('/random', response_model=Joke)
async def get_random_joke():
    result = await db.random_document()
    return {
        'status': 'OK',
        'result': result
    }


@router.get('/{joke_id}', response_model=Joke)
async def get_joke_by_id(joke_id: str):
    result = await db.find(joke_id)
    return {
        'status': 'OK',
        'result': result
    }



