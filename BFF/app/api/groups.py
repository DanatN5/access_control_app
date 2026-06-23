from typing import Annotated

from fastapi import Depends, APIRouter

from app.dependencies import get_client
from app.schemas.group_schemas import GroupRead, GroupCreate
from app.client import HttpClient
from app.config import settings

groups = APIRouter()

ClientDependency = Annotated[HttpClient, Depends(get_client)]

URL = f"{settings.registry_url}/groups"


@groups.post("/groups")
async def create_group(
    client: ClientDependency,
    group: GroupCreate
) -> GroupRead:
    return await client.send(URL, group)

@groups.get("/groups")
async def get_groups_list(client: ClientDependency) -> list[GroupRead]:
    return await client.get(URL)

@groups.get("/groups/{group_id}")
async def get_user_by_id(
    client: ClientDependency,
    group_id: int
) -> GroupRead:
    url = f"{URL}/{group_id}"
    return await client.get(url)