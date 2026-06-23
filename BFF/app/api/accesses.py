from typing import Annotated

from fastapi import Depends, APIRouter

from app.dependencies import get_client
from app.schemas.access_schemas import AccessRead
from app.client import HttpClient
from app.config import settings

accesses = APIRouter()

ClientDependency = Annotated[HttpClient, Depends(get_client)]

URL = f"{settings.registry_url}/accesses"

@accesses.get("/accesses")
async def get_accesses_list(client: ClientDependency) -> list[AccessRead]:
    return await client.get(URL)