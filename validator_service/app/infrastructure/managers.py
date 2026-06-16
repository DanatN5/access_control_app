from app.infrastructure.client import HttpxClient
from app.exceptions import NotFoundError

class RegistryManager:

    def __init__(self, client: HttpxClient, url: str):
        self.url = url
        self.client = client

    async def exists(self, resource: str, id: int) -> bool:
        try:
            response = await self.client.get(
                f"{self.url}/{resource}/{id}"
            )

            return True
        
        except NotFoundError:
            return False


        
