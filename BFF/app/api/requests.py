from typing import Annotated

from fastapi import Depends, APIRouter

from app.dependencies import get_client
from app.schemas.request_schemas import RequestRead, RequestReadShort
from app.client import HttpClient
from app.config import settings

requests = APIRouter()

ClientDependency = Annotated[HttpClient, Depends(get_client)]

URL = f"{settings.registry_url}/requests"

@requests.get("/requests")
async def get_requests(client: ClientDependency) -> list[RequestReadShort]:
    return await client.get(URL)


@requests.get("/requests/{request_id}")
async def get_request_by_id(
    request_id: int,
    client: ClientDependency
) -> RequestRead:
    url = f"{URL}/{request_id}"
    return await client.get(url)

