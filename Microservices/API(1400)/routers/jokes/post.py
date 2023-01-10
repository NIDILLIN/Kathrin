import aiohttp
from fastapi import APIRouter

from models import UploadJoke, Joke
from config import settings


router = APIRouter()


@router.post("/jokes/create_joke", response_model=Joke)
async def create_joke(joke: UploadJoke):
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
    """
    async with aiohttp.ClientSession() as session:
        async with session.post(
            settings.jokes+settings.Methods.Jokes.Post.create_joke,
            json=joke.dict()
        ) as resp:
            r = await resp.json()

    return r


