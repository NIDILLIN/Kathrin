import datetime
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings
from models import Boar, Category, UploadBoar, UploadCategory


class DB:
    __slots__ = ('db', 'boars', 'categories')

    def __init__(self) -> None:
        client = AsyncIOMotorClient(
            settings.mongo_host, 
            settings.mongo_port
        )
        self.db = client['main_boars']
        self.boars = self.db['boars']
        self.categories = self.db['categories']

    async def get_documents(self, skip: int = 0, limit: int = 10):
        cursor = self.boars.find()
        cursor.skip(skip).limit(limit)

        count = await self.boars.count_documents({})

        result = []
        async for document in cursor:
            document['id'] = str(document.pop('_id'))
            result.append(document)

        return count, result

    async def save_category(self, category: UploadCategory):
        document = category.dict()
        document['created_at'] = datetime.date.today().strftime('%Y-%m-%d')
        r = await self.categories.insert_one(
            document
        )
        document['id'] = str(document.pop('_id'))
        return document

    async def random_document(self):
        cursor = self.boars.aggregate([{ '$sample': { 'size': 1 } }])
        documents = await cursor.to_list(length=None)
        document = documents[0]
        document['id'] = str(document.pop('_id'))
        return document

    async def find(self, boar_id: str):
        document = await self.boars.find_one({'_id': ObjectId(boar_id)})
        document['id'] = str(document.pop('_id'))
        return document

    async def save_document(self, boar: UploadBoar) -> str:
        document = boar.dict()
        document['created_at'] = datetime.date.today().strftime('%Y-%m-%d')
        
        r = await self.boars.insert_one(
            document
        )
        document['id'] = str(document.pop('_id'))
        return document



db = DB()