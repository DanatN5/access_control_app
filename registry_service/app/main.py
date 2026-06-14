from fastapi import FastAPI
from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator
from app.api.users import users
from app.api.groups import groups
from app.api.accesses import accesses
from app.broker.faststream_broker import broker

app = FastAPI()
app.include_router(router=users, prefix="/v1")
app.include_router(router=accesses, prefix="/v1")
app.include_router(router=groups, prefix="/v1")

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    await broker.start()

    yield

    await broker.stop()



@app.get("/health")
async def check_health():
    return {'status': "ok"}

