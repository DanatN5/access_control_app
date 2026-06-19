from app.infrastructure.client import HttpClient
from app.messaging.schemas import Request
from app.application.service import ValidationService
from app.infrastructure.managers import UserManager

class RequestHandler:
    
    validated: bool = None
    errors: list[str] = []

    def __init__(
            self,
            mapper: dict,
            client: HttpClient,
            validator: ValidationService):
        self.client = client
        self.validator = validator(self.client)
        self.user_mgr = UserManager(self.client)

    async def handle(self, request: Request):
        user_id = request.user_id
        if not await self.user_mgr.exists(user_id):
            self.errors.append(f"User {user_id} doesn't exist")
            self.validated = False
            
        else:

            if request.action == "grant access":
                await self.__annotations__

    async def grant_access(self, user_id: int, accesses_id: list[int]) -> None:
        if not await self.access_mgr.exists(accesses_id):
            self.errors.append("Accesses dont exist")
            self.validated = False
        user_group = await self.user_mgr.get_info(user_id, "group")
        for access in accesses_id:
            if access in user_group.forbidden_accesses:
                self.errors.append("Accesses is not allowed for user's group")
                self.validated = False
        
        await self.user_mgr.grant_access(user_id, accesses_id)




