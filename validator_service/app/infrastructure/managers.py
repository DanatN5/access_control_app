from app.infrastructure.client import HttpxClient
from app.exceptions import NotFoundError

class RegistryManager:
    
    resource: str

    def __init__(self, client: HttpxClient, url: str):
        self.url: str = url
        self.client: HttpxClient = client
        

    async def exists(self, id: int) -> bool:
        try:
            response = await self.client.get(
                f"{self.url}/{self.resource}/{id}"
            )

            return True
        
        except NotFoundError:
            return False


class UserManager(RegistryManager):

    resource = "users"

    async def get_info(self, user_id: int, info: str) -> list:
        try:
            response = await self.client.get(
                f"{self.url}/{self.resource}/{user_id}/{info}"
            )
            return response
        except Exception:
            pass


class AccessManager(RegistryManager):

    resource = "accesses"

    async def exists(self, ids: list[int]):
        try:
            errors = []
            response = await self.client.get(
                f"{self.url}/{self.resource}"
            )
            existing_accesses = [access["id"] for access in response]
            
            for id in ids:
                if id not in existing_accesses:
                    errors.append(id)
                
            return errors
        
        except Exception:
            pass


class GroupManager(RegistryManager):

    resource = "groups"
