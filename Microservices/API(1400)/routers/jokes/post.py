from fastapi import APIRouter

from models import JokePackage, Joke
from config import settings
from session import get_session


router = APIRouter()


@router.post("/jokes/create_joke", response_model=JokePackage)
async def create_joke(jokePackage: Joke):
    session = get_session()
    async with session.get(
        settings.jokes+settings.Methods.Jokes.Post.create_joke) as resp:

        r = await resp.json()

    return r


