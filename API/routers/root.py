import aiohttp

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from config import settings

from models import NewUser


router = APIRouter()


@router.get('/')
async def get_root():
    return RedirectResponse(settings.self_url+'redoc/')


@router.get("/createUser", response_model=NewUser)
async def get_uuid(*, username: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(settings.api_url) as resp:
            r = await resp.json()

    return NewUser(
        user_id=r['user_id'],
        username=username,
        token=r['token'],
        signedAt=r['date']
    )