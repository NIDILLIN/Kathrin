from fastapi import FastAPI

from routers import get, post, put


app = FastAPI()

app.include_router(get.router)
app.include_router(post.router)
app.include_router(put.router)
