from fastapi import FastAPI
from app.api.users import users
from app.api.groups import groups
from app.api.accesses import accesses

app = FastAPI()
app.include_router(router=users, prefix="/v1")
app.include_router(router=accesses, prefix="/v1")
app.include_router(router=groups, prefix="/v1")

@app.get("/health")
async def check_health():
    return {'status': "ok"}

