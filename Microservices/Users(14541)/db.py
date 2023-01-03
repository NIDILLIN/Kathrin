from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from config import settings
from models import NewUser, User, Wct


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

    async def random_document(self):
        cursor = self.collection.aggregate([{ '$sample': { 'size': 1 } }])
        documents = await cursor.to_list(length=None)
        document = documents[0]
        document.pop('_id')
        return document

    async def find(self, syncId: str):
        document = await self.collection.find_one({'syncId': syncId})
        document.pop('_id')
        return document

    async def create_user(self, user: NewUser) -> str:
        document = User(
            syncId=user.syncId,
            username=user.username,
            registration_date=user.registration_date
        ).dict()

        document['registration_date'] = document['registration_date'].isoformat()
        
        r = await self.collection.insert_one(
            document
        )
        return document['syncId']

    async def get_user_wct(self, syncId: int) -> dict:
        document = await self.collection.find_one({'syncId': syncId})
        wct = document.get('wct')
        return wct

    async def update_user_wct(self, syncId: int, wct: Wct):
        wct = wct.dict()
        wct['given_date'] = wct['given_date'].isoformat()

        await self.collection.find_one_and_update(
            {'syncId': syncId}, 
            {'$set': {
                'wct': wct
            }}
        )

    async def save_avatar(self, syncId: int):
        ...



db = DB()