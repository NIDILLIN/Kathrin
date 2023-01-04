import os
import random
from fastapi import APIRouter
import openai

from models import Message


router = APIRouter()
openai.api_key = os.getenv('API_KEY')


@router.post('/message')
async def get_all_boars(message: Message):
    response = await get_answer(message)
    return response


async def get_answer(message: Message):
    response = openai.Completion.create(
        **message.dict()
    )
    return response['choices'][0]['text']

# {
#   "model": "text-davinci-003",
#   "prompt": ...,
#   "temperature": 0.5,
#   "max_tokens": 350,
#   "top_p": 1.0,
#   "frequency_penalty": 0.0,
#   "presence_penalty": 0.0
# }