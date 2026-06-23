from typing import Protocol
import httpx
from app.exceptions import NotFoundError


class HttpClient(Protocol):
    async def get(self, url: str) -> dict: ...

    async def send(self, url: str, payload: dict) -> None: ...

class HttpxClient:

    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    async def get(self, url: str) -> dict:

        response = await self.client.get(url)

        if response.status_code == 404:
            raise NotFoundError()

        response.raise_for_status()

        return response.json()
    
    
    async def send(self, url: str, payload: dict) -> None:
        await self.client.post(url, json=payload.model_dump(mode="json"))
