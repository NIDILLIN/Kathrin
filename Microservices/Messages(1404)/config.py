import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    mongo_host: str
    mongo_port: int


settings = Settings(
    mongo_host=os.environ.get('MONGO_HOST'),
    mongo_port=os.environ.get('MONGO_PORT')
)