import aiofiles
from fastapi import APIRouter

from models import JokePackage
from db import db


router = APIRouter()


@router.post("/jokes/")
async def create_joke(jokePackage: JokePackage):
    """ Example JSON POST to create joke record at DataBase
    {
        'joke': 'string'
        'date': '2022-12-30
        'uploaded_by': {
            'id': 16231246,
            'username': 'username',
            'registration_date': '2021-08-12'
        }
}
    """
    id = await db.save_document(jokePackage)
    return {
        'status': 'OK',
        'joke_id': id
    }


