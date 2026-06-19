from app.infrastructure.client import HttpClient
from app.infrastructure.managers import (
    RegistryManager,
    UserManager,
    AccessManager,
    GroupManager,
)
from app.messaging.schemas import Request, RequestValidatedEvent


class ValidationService:

    user_manager = UserManager
    access_manager = AccessManager
    group_manager = GroupManager

    def __init__(self, client: HttpClient):
        self.client = client
        
    
    async def process_request(self, request: Request): ...

    