import aiofiles
from fastapi import APIRouter, UploadFile

from config import settings
from session import get_session


router = APIRouter()


@router.post("/photos/create_photo")
async def create_upload_file(file: UploadFile):
    session = get_session()
    async with session.post(
        url=settings.photos+settings.Methods.Photos.Post.create_photo,
        data=file) as resp:

        r = await resp.json()

    return r


