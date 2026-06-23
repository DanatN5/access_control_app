from app.infrastructure.client import HttpClient
from app.messaging.schemas import Request, RequestValidatedEvent
from app.application.service import ValidationService
from app.config import settings


class RequestHandler:
    
    def __init__(
            self,
            client: HttpClient,
            validator: ValidationService):
        self.client = client
        self.validator = validator
        self.validated = True
        self.errors = ""
        self.cases = {
            "grant access": self.grant_access,
            "revoke access": self.revoke_access,
            "reset group": self.reset_group,
            "unset group": self.unset_group,
        }
    

    def get_validation_result(self, request: Request) -> RequestValidatedEvent:
        return {
            "validated": self.validated,
            "errors": self.errors,
            "user_id": request.user_id,
            "action": request.action,
            "accesses_ids": request.accesses_ids,
            "group_id": request.group_id,
        }
    

    async def handle(self, request: Request):
        user_id = request.user_id
        if not await self.validator.user_exists(user_id):
            self.errors = f"User {user_id} doesn't exist"
            self.validated = False
            
        else:
            await self.cases[request.action](request)

        message = self.get_validation_result(request)

        await self.send_result(message)


    async def grant_access(self, request: Request) -> None:
        access_errors = await self.validator.access_exists(request.accesses_ids)
        if access_errors:
            self.errors = f"Accesses {access_errors} don't exist"
            self.validated = False
        
        if await self.validator.is_user_access(request.user_id, request.accesses_ids):
            self.errors = f"User {request.user_id} already have these accesses"
            self.validated = False

        if await self.validator.is_access_forbidden_for_user(
            request.user_id,
            request.accesses_ids
        ):
            self.errors = "Accesses is not allowed for user's group"
            self.validated = False
    
    
    async def revoke_access(self, request: Request) -> None:
        access_errors = await self.validator.access_exists(request.accesses_ids)
        if access_errors:
            self.errors = f"Accesses {access_errors} don't exist"
            self.validated = False
        
        if not await self.validator.is_user_access(request.user_id, request.accesses_ids):
            self.errors = f"User {request.user_id} doesn't have these accesses"
            self.validated = False

    
    async def reset_group(self, request: Request) -> None:
        if not await self.validator.group_exists(request.group_id):
            self.errors = f"Group {request.group_id} doesn't exist"
            self.validated = False
        if await self.validator.is_user_group(request.user_id, request.group_id):
            self.errors = f"User {request.user_id} is already in group {request.group_id}"
            self.validated = False

    
    async def unset_group(self, request: Request) -> None:
        if not await self.validator.group_exists(request.group_id):
            self.errors = f"Group {request.group_id} doesn't exist"
            self.validated = False
        if not await self.validator.is_user_group(request.user_id, request.group_id):
            self.errors = f"User {request.user_id} is not in group {request.group_id}"
            self.validated = False 


    async def send_result(self, msg: RequestValidatedEvent):
        await self.client.send(f"{settings.request_url}/v1/requests", msg)
        






