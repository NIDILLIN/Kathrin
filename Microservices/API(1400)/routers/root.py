from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse

from config import settings
from models import NewUser
from session import get_session

router = APIRouter()


@router.get('/')
async def get_root():
    return RedirectResponse(settings.api+'docs/')


@router.post("/create_user", response_model=NewUser)
async def get_uuid(*, username: str):
    session = get_session()
    async with session.post(
        settings.users+settings.Methods.Users.Post.create_user, 
        data={'username': username}) as resp:

        r = await resp.json()

    return NewUser(
        user_id=r['user_id'],
        username=username,
        token=r['token'],
        registration_date=r['date']
    )

