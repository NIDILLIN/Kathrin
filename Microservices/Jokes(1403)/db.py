import datetime
from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings
from models import UploadJoke



class DB:
    __slots__ = ('db', 'collection')

    def __init__(self) -> None:
        client = AsyncIOMotorClient(
            settings.mongo_host, 
            settings.mongo_port
        )
        self.db = client['main_jokes']
        self.collection = self.db['jokes']

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

    async def random_document(self):
        cursor = self.collection.aggregate([{ '$sample': { 'size': 1 } }])
        documents = await cursor.to_list(length=None)
        document = documents[0]
        document['id'] = str(document.pop('_id'))
        return document

    async def save_document(self, joke: UploadJoke) -> str:
        document = joke.dict()
        document['created_at'] = datetime.date.today().strftime('%Y-%m-%d')
        document['uploaded_by']['registration_date'] = document['uploaded_by']['registration_date'].strftime('%Y-%m-%d')
        
        r = await self.collection.insert_one(
            document
        )
        document['id'] = str(document.pop('_id'))
        return document



db = DB()