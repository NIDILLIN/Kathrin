from fastapi import FastAPI

from routers import get


app = FastAPI()

app.include_router(get.router)
