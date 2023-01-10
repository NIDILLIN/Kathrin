from fastapi import APIRouter

from models import UploadJoke, Joke
from db import db


router = APIRouter()


@router.post("/create_joke", response_model=Joke)
async def create_joke(uploadJoke: UploadJoke):
    joke = await db.save_document(uploadJoke)
    return joke


