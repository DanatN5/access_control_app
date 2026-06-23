from typing import Annotated

from fastapi import Depends, APIRouter

from app.dependencies import get_client
from app.schemas.user_schemas import UserRead
from app.schemas.group_schemas import GroupRead
from app.schemas.access_schemas import AccessRead
from app.client import HttpClient
from app.config import settings

users = APIRouter()

ClientDependency = Annotated[HttpClient, Depends(get_client)]

URL = f"{settings.registry_url}/users"

@users.get("/users")
async def get_users(client: ClientDependency) -> list[UserRead]:
    users = await client.get(URL)

    return users

@users.get("/users/{user_id}")
async def get_user_by_id(user_id: int, client: ClientDependency) -> UserRead:
    url = f"{URL}/{user_id}"
    return await client.get(url)

@users.get("/users/{user_id}/group")
async def get_user_group(user_id: int, client: ClientDependency) -> GroupRead:
    url = f"{URL}/{user_id}/group"
    return await client.get(url)

@users.get("/users/{user_id}/accesses")
async def get_user_accesses(user_id: int, client: ClientDependency) -> list[AccessRead]:
    url = f"{URL}/{user_id}/accesses"
    return await client.get(url) 
