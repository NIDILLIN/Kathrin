from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings
from models import User, External



class DB:
    __slots__ = ('db', 'collection')

    def __init__(self) -> None:
        client = AsyncIOMotorClient(
            settings.mongo_host, 
            settings.mongo_port
        )
        self.db = client['main_auth']
        self.collection = self.db['users']

    async def find(self, user_id: str):
        document = await self.collection.find_one({'id': user_id})
        document.pop('_id')
        return document

    async def find_user(self, external: External):
        document = await self.collection.find_one({external.type: external.id})
        syncId = document.get('syncId', None)
        return syncId

    async def save_document(self, user: dict) -> str:
        r = await self.collection.insert_one(
            user
        )
        user.pop('_id')
        return user



db = DB()