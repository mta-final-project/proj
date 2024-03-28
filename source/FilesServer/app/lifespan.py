from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.mongo import init
from app.settings import get_settings


async def on_start(_app: FastAPI):
    settings = get_settings()
    await init(settings.mongo.url, settings.mongo.database)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await on_start(app)
    yield
