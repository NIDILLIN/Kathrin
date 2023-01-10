import aiohttp
from fastapi import APIRouter, UploadFile

from config import settings
from models import Photo


router = APIRouter()


@router.post("/photos/create", response_model=Photo)
async def create_upload_file(syncId: int, username: str, file: UploadFile):
    """
    {
        'status': 'OK',
        'result': {
            'id': str,
            'filename': str, 
            'created_at': datetime.date (YYYY-MM-DD),
            'uploaded_by': {
                'syncId': int,
                'username': str
            }
        }
    }
    """
    file_bytes = await file.read()
    async with aiohttp.ClientSession() as session:
        async with session.post(
            settings.photos+settings.Methods.Photos.Post.upload_photo(syncId=syncId, username=username),
            data=file_bytes
        ) as resp:
            r = await resp.json()

    return r