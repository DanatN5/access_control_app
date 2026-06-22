from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator
from app.exceptions import NotFoundError
from app.messaging.fs_broker import broker
from app.api.publish import publish
# from app.api.users import users
# from app.api.groups import groups
# from app.api.accesses import accesses
# from app.api.requests import requests
# from app.exceptions.exceptions import NotFoundError


app = FastAPI()
app.include_router(router=publish, prefix="/v1")
# app.include_router(router=users, prefix="/v1")
# app.include_router(router=accesses, prefix="/v1")
# app.include_router(router=groups, prefix="/v1")
# app.include_router(router=requests, prefix="/v1")

@app.exception_handler(NotFoundError)
async def not_found_handler(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)}
    )

@asynccontextmanager
async def lifespan(app: FastAPI):
    await broker.start()
    yield
    await broker.stop()

app = FastAPI(lifespan=lifespan)



@app.get("/health")
async def check_health():
    return {'status': "ok"}