from fastapi import FastAPI

from routers.include import include_routers


app = FastAPI()

include_routers(app)
