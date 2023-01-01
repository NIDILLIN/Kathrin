from pydantic import BaseSettings


class Settings(BaseSettings):
    self_url: str
    api_url: str
    
    class Config:
        env_file = '.env'


settings = Settings()
