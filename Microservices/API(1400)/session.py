import aiohttp


def get_session():
    return aiohttp.ClientSession()