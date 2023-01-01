from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings
from models import User



class DB:
    __slots__ = ('db', 'collection')

    def __init__(self) -> None:
        client = AsyncIOMotorClient(
            settings.mongo_host, 
            settings.mongo_port
        )
        self.db = client['main_users']
        self.collection = self.db['users']

    async def get_documents(self, skip: int = 0, limit: int = 10):
        cursor = self.collection.find()
        cursor.skip(skip).limit(limit)

        count = await self.collection.count_documents({})

        result = []
        async for document in cursor:
            document.pop('_id')
            result.append(document)

        return count, result

    async def find(self, user_id: str):
        document = await self.collection.find_one({'id': user_id})
        document.pop('_id')
        return document

    async def random_document(self):
        cursor = self.collection.aggregate([{ '$sample': { 'size': 1 } }])
        documents = await cursor.to_list(length=None)
        document = documents[0]
        document.pop('_id')
        return document

    async def save_document(self, user: User) -> str:
        document = user.dict()
        document['registration_date'] = document['registration_date'].isoformat()
        
        r = await self.collection.insert_one(
            document
        )



db = DB()