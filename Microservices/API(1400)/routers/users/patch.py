from fastapi import APIRouter

from models import Wct
from config import settings
from session import get_session


router = APIRouter()


@router.patch("/users/{syncId}/wct")
async def update_wct(syncId: int, wct: Wct):
    session = get_session()
    async with session.patch(
        url=settings.users+settings.Methods.Users.Patch.user_wct(syncId=syncId),
        data=wct.dict()) as resp:

        r = await resp.json()

    return r


