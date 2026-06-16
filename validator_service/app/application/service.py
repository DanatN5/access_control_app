from app.infrastructure.client import HttpClient
from app.messaging.schemas import Request, RequestValidatedEvent

class ValidationService:
    def __init__(self, client: HttpClient):
        self.client = client

    async def validate_by_id(self, id: int, manager) -> RequestValidatedEvent:
        errors = []
        if not await self.client.user_exists(data.user_id):
            errors.append("User doesn't esxist")
        
        return RequestValidatedEvent(
            request_id = data
        )
    
    async def process_request(self, request: Request): ...
    