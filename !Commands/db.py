from fastapi import UploadFile
from motor.motor_asyncio import AsyncIOMotorClient
from config import settings


class DB:
    __slots__ = ('db', 'collection')

    def __init__(self) -> None:
        client = AsyncIOMotorClient(
            settings.mongo_host, 
            settings.mongo_port
        )
        self.db = client['main_photos']
        self.collection = self.db['photos']

    async def get_photos(self, skip: int = 0, limit: int = 10):
        cursor = self.collection.find()
        cursor.skip(skip).limit(limit)

        count = await self.collection.count_documents({})

        result = []
        async for document in cursor:
            document['_id'] = str(document['_id'])
            result.append(document)

        return count, result

    async def random_photo(self):
        cursor = self.collection.aggregate([{ '$sample': { 'size': 1 } }])
        documents = await cursor.to_list(length=None)
        document = documents[0]
        document['_id'] = str(document['_id'])
        return document

    async def save(self, photo: UploadFile) -> str:
        r = await self.collection.insert_one({'name': photo.filename})
        id = r.inserted_id
        return id



db = DB()