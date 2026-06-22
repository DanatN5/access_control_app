from app.infrastructure.client import HttpClient
from app.infrastructure.managers import (
    UserManager,
    AccessManager,
    GroupManager,
)
from app.config import settings

REQUEST_URL = f"{settings.request_url}/v1"

class ValidationService:

    validated: bool = None
    errors: list[str] = []

    def __init__(self, client: HttpClient):
        self.client = client
        self.user_mgr = UserManager(self.client, REQUEST_URL)
        self.access_mgr = AccessManager(self.client, REQUEST_URL)
        self.group_mgr = GroupManager(self.client, REQUEST_URL)
        
    
    async def user_exists(self, id: int) -> bool:
        return await self.user_mgr.exists(id)
    
    async def access_exists(self, ids: list[int]) -> list:
        return await self.access_mgr.exists(ids)
    
    async def group_exists(self, id: int) -> bool:
        return await self.group_mgr.exists(id)
    
    async def is_access_forbidden_for_user(self, user_id: int, access_ids: list[int]) -> bool:
        user_group = await self.user_mgr.get_info(user_id, "group")
        for access in access_ids:
            if access in user_group.forbidden_accesses:
                return True
        return False
    
    async def is_user_access(self, user_id: int, access_ids: list[int]) -> bool:
        user_accesses = await self.user_mgr.get_info(user_id, "accesses")
        for access in access_ids:
            if access not in user_accesses:
                return False
        return True
    
    async def is_user_group(self, user_id: int, group_id: int) -> bool:
        user_group = await self.user_mgr.get_info(user_id, "group")
        if group_id == user_group.id:
            return True
        return False
    
    
