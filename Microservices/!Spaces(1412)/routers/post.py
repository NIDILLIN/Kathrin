from fastapi import APIRouter

from models import JokePackage
from db import db


router = APIRouter()


@router.post("/create_joke")
async def create_joke(jokePackage: JokePackage):
    """ Example JSON POST to create joke record at DataBase
    {
        'joke': 'string'
        'date': '2022-12-30
        'uploaded_by': {
            'id': 16231246,
            'username': 'username',
        }
}
    """
    id = await db.save_document(jokePackage)
    return {
        'status': 'OK',
        'joke_id': id
    }


