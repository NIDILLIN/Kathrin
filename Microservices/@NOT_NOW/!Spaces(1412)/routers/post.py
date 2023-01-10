from fastapi import APIRouter

from models import JokePackage
from db import db


router = APIRouter()


@router.post("/create_space")
async def create_joke(space):
    ...

