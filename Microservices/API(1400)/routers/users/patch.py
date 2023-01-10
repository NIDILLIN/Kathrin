import aiohttp
from fastapi import APIRouter

from models import Wct
from config import settings


router = APIRouter()


@router.patch("/users/{syncId}/wct")
async def update_wct(syncId: int, wct: Wct):
    """
    {
        'status': 'OK'
    }
    """
    async with aiohttp.ClientSession() as session:
        async with session.patch(
            settings.users+settings.Methods.Users.Patch.user_wct(syncId=syncId),
            json=wct.dict()    
        ) as resp:
            r = await resp.json()
    
    return r

