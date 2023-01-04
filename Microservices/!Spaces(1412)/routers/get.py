from fastapi import APIRouter

from db import db


router = APIRouter()


@router.get('/filter', response_model=list[str])
async def get_jokes_with_params(*, skip: int, limit: int):
    _, result = await db.get_documents(skip=skip, limit=limit)
    return result


@router.get('/')
async def get_all_jokes():
    count, result = await db.get_documents(skip=0, limit=10)
    return {
        'count': count,
        'jokes': result
    }


@router.get('/random')
async def get_random_joke():
    result = await db.random_document()
    return result


@router.get('/{joke_id}')
async def get_joke_by_id(joke_id: str):
    jokePackage = await db.find(joke_id)
    return jokePackage



