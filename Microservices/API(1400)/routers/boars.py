from fastapi import APIRouter

from config import settings


router = APIRouter()


@router.get('/boars')
async def get_boars():
    return {        

    }