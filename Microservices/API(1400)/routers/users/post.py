import aiofiles
from fastapi import APIRouter, UploadFile

from models import NewUser
from config import settings
from session import get_session


router = APIRouter()


@router.post("/users/{syncId}/avatar")
async def create_user_avatar(syncId: int, file: UploadFile):
    session = get_session()
    async with session.post(
        url=settings.users+settings.Methods.Users.Post.avatar(syncId=syncId),
        data=file) as resp:

        r = await resp.json()

    return r


