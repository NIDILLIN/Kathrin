import aiohttp
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from config import settings
from models import External, User

router = APIRouter()


@router.get('/')
async def get_root():
    return RedirectResponse(settings.api+'docs/')


@router.post("/create_user", response_model=User)
async def create_new_user(username: str, external: External = None):
    """
    What is External?
        External is json that contains type of social media and id that user have.
        {
            "type": "telegram",
            "id": 1631513712
        }

    If external_id is None (telegram_id, vk_id) then auth server will just create new user,
    Else auth server will aggregate created itself syncId with external_id and return
    the syncId that will be match external_id.

    Then resource Users will create record about that user with only syncId.
    """
    if external is not None: 
        external = external.dict()

    async with aiohttp.ClientSession() as session:
        async with session.post(settings.authserver+settings.Methods.Auth.Get.new_user,
        json=external
        ) as resp:
            auth_resp = await resp.json()

    post_user = auth_resp
    post_user['username'] = username

    async with aiohttp.ClientSession() as session:
        async with session.post(
            settings.users+settings.Methods.Users.Post.create_user,
            json=post_user
            ) as resp:
            user = await resp.json()


    return user


@router.get("/match_user")
async def match_id_to_syncId(*, some_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            settings.authserver+settings.Methods.Auth.Get.match(external_id=some_id)    
        ) as resp:
            r = await resp.json()
    syncId = r['syncId']

    return syncId