from fastapi import FastAPI

from routers import boars
from routers import jokes
from routers import photos
from routers import users
from routers import commands
from routers import root


def include_routers(app: FastAPI):
    app.include_router(root.router)
    app.include_router(boars.get.router)
    app.include_router(boars.post.router)

    app.include_router(jokes.get.router)
    app.include_router(jokes.post.router)

    app.include_router(photos.get.router)
    app.include_router(photos.post.router)

    app.include_router(users.get.router)
    app.include_router(users.post.router)
    app.include_router(users.patch.router)

    app.include_router(commands.get.router)
