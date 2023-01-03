import aiohttp

from config import settings

def get_session():
    return aiohttp.ClientSession()