import os
import random
from fastapi import APIRouter
import openai

from models import Message


router = APIRouter()
openai.api_key = os.getenv('API_KEY')


@router.get('/message')
async def get_all_boars(message: Message):
    response = await get_answer(message)
    return response


async def get_answer(message: Message):
    response = openai.Completion.create(
        **message.dict()
    )
    count = len(response['choices'])
    index = random.randint(0, count)
    return response['choices'][index]['text']
