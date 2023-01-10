import hashlib
import datetime
from fastapi import UploadFile
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings
from models import UploadPhoto, UploadUser, Photo


def Hash(string: str):
    hash = hashlib.sha256(string.encode('utf-8')).digest().decode('utf-8')
    return hash


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
            document['id'] = str(document.pop('_id'))
            result.append(document)

        return count, result

    async def random_photo(self):
        cursor = self.collection.aggregate([{ '$sample': { 'size': 1 } }])
        documents = await cursor.to_list(length=None)
        document = documents[0]
        document['id'] = str(document.pop('_id'))
        return document

    async def save(self, user: UploadUser, file: UploadFile) -> Photo:
        filename = await Hash(file.filename)
        filename += '.png'
        uploadUser = user.dict()
        
        document = {
            'filename': filename,
            'created_at': datetime.date.today().strftime('%Y-%m-%d'),
            'uploaded_by': uploadUser
        }
        r = await self.collection.insert_one(
            document
        )
        document['id'] = str(document.pop('_id'))

        return document



db = DB()