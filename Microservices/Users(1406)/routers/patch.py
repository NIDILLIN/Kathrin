from fastapi import APIRouter

from db import db
from models import Wct

router = APIRouter()


@router.patch("/{syncId}/wct")
async def update_wct(syncId: int, wct: Wct):
    await db.update_user_wct(syncId, wct)
    return {
        'status': 'OK'
    }


