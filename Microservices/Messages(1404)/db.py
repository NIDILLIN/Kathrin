from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings
from models import Message



class DB:
    __slots__ = ('db', 'collection')

    def __init__(self) -> None:
        client = AsyncIOMotorClient(
            settings.mongo_host, 
            settings.mongo_port
        )
        self.db = client['main_messages']
        self.collection = self.db['messages']

    async def get_documents(self, skip: int = 0, limit: int = 10):
        cursor = self.collection.find()
        cursor.skip(skip).limit(limit)

        count = await self.collection.count_documents({})

        result = []
        async for document in cursor:
            document['id'] = str(document.pop('_id'))
            result.append(document)

        return count, result

    async def find(self, joke_id: str):
        document = await self.collection.find_one({'_id': ObjectId(joke_id)})
        document['id'] = str(document.pop('_id'))
        return document

    async def save(self, message: Message) -> str:
        document = message.dict()
        document['date'] = document['date'].isoformat()
        document['uploaded_by']['registration_date'] = document['uploaded_by']['registration_date'].isoformat()
        
        r = await self.collection.insert_one(
            document
        )
        id = str(r.inserted_id)
        return id



db = DB()