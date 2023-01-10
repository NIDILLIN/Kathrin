import datetime
from typing import Union
from bson import ObjectId

from fastapi import APIRouter

from db import db
from models import User, NewUser, External


router = APIRouter()



@router.post("/new_user")
async def new_user(*, external: Union[External, None] = None):
    date = datetime.datetime.today().strftime('%Y-%m-%d')
    uuid = gen_uuid()
    # token = gen_token()
    user = {
        'syncId': uuid,
        'registration_date': date
    }
    if external is not None:
        user[external.type] = external.id
    user = await db.save_document(user)

    return user


@router.get("/match_user", response_model=int)
async def new_user(*, external_id: int = None):
    syncId = await db.find_user(external_id)
    
    return syncId


def gen_uuid():
    date = datetime.datetime.now()
    id = datetime.datetime.timestamp(date)*100
    id = int(id)
    return id


def gen_token():
    a = ObjectId()
    b = ObjectId()
    token = str(a) + str(b)
    return token
