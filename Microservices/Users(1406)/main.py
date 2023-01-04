from fastapi import FastAPI

from routers import get, patch, post


app = FastAPI()

app.include_router(get.router)
app.include_router(post.router)
app.include_router(patch.router)
