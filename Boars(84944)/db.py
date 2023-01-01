from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings
from models import Boar, Category


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

    async def get_categories(self):
        cursor = self.categories.find()

        count = await self.categories.count_documents({})

        result = []
        async for document in cursor:
            document.pop('_id')
            result.append(document)

        return count, result

    async def save_category(self, category: Category):
        document = category.dict()
        document['created_date'] = document['created_date'].isoformat()
        r = await self.categories.insert_one(
            document
        )

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

    async def save_document(self, boar: Boar) -> str:
        document = boar.dict()
        document['created_date'] = document['created_date'].isoformat()
        document['created_by']['registration_date'] = document['created_by']['registration_date'].isoformat()
        
        r = await self.boars.insert_one(
            document
        )
        id = str(r.inserted_id)
        return id



db = DB()