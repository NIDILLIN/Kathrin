from fastapi import APIRouter

from db import db
from models import Message

router = APIRouter()


@router.get('/messages', response_model=list[str])
async def get_messages_with_params(*, skip: int, limit: int):
    _, result = await db.get_documents(skip=skip, limit=limit)
    return result


@router.get('/messages/')
async def get_all_messages():
    count, result = await db.get_documents(skip=0, limit=10)
    return {
        'count': count,
        'messages': result
    }


@router.get('/messages/{message_id}', response_model=Message)
async def get_joke_by_id(message_id: str):
    message = await db.find(message_id)
    return message



