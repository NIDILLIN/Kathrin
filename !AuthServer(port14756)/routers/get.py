from bson import ObjectId
import datetime
from fastapi import APIRouter

from db import db
from models import User


router = APIRouter()


@router.get("/uuid", response_model=User)
async def get_uuid():
    date = datetime.datetime.now()
    id = gen_uuid()
    token = gen_token()
    new_user = User(
        id=id,
        token=token,
        registration_date=date
    )
    await save_data(new_user)

    return new_user


async def save_data(user: User):
    await db.save_document(user)


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
