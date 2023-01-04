import typing as tp
from pydantic import BaseSettings


class Urn: 
    urn: str
    uri: str

    def __init__(self, urn: str) -> None:
        self.uri = urn

    def __call__(self, **kwargs):
        if kwargs is None:
            return self.uri
        return self.uri.format(**kwargs)


class Settings(BaseSettings):
    api: str
    users: str
    boars: str
    jokes: str
    photos: str
    commands: str
    uploader: str
    chatbot: str
    collector: str
    authserver: str
    messages: str
    achievements: str

    class Methods:
        class Users:
            class Post:
                create_user = 'create_user'
                avatar = Urn('{syncId}/avatar')

            class Get:
                users = ''
                filter = Urn('filter?skip={skip}&limit={limit}')
                random = 'random'
                user = Urn('{syncId}')
                user_wct = Urn('{syncId}/wct')
                avatar = Urn('{syncId}/avatar')

            class Patch:
                user_wct = Urn('{syncId}/wct')
    
        class Photos:
            class Get:
                photos = ''
                filter = Urn('filter?skip={skip}&limit={limit}')
                random = 'random'
                photo = Urn('{photo_path}')
            
            class Post:
                create_photo = 'create_photo'

        class Jokes:
            class Get:
                jokes = ''
                filter = Urn('filter?skip={skip}&limit={limit}')
                random = 'random'
                joke = Urn('{joke_id}')

            class Post:
                create_joke = 'create_joke'

        class Chatbot:
            class Get:
                message = 'message'

        class Boars:
            class Get:
                boars = ''
                filter = Urn('filter?skip={skip}&limit={limit}')
                random = 'random'
                boar = Urn('{boar_id}')
                file = Urn('{boar_id}/file')
                categories = 'categories'

            class Post:
                create_boar = 'create_boar'
                create_file = Urn('{boar_id}/file')
                create_categoria = 'categories/create'

        class Commands:
            class Get:
                wct = 'wct'
                photo = 'photo'
                joke = 'joke'
                boars = 'boars'
                user_status = 'userstatus'


    class Config:
        env_file = '.env'


settings = Settings()
