from app.repositories.uow import UnitOfWork
from app.schemas.request_schemas import ValidatedRequest, RequestCreate
from app.models import Request

class RequestService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    
    async def process_request(self, request: ValidatedRequest) -> None:
        
        if request.validated:
            action = request.action
            await getattr(self, action)(request)
        
        await self.update_request_status(request)


    async def grant_access(self, request: ValidatedRequest) -> None:
        accesses = await self.uow.accesses.get_many(request.accesses_ids)
        user = await self.uow.users.get(request.user_id, eager=True)
        user.accesses.extend(accesses)

    
    async def revoke_accesses(self, request: ValidatedRequest) -> None:

        accesses = await self.uow.accesses.get_many(request.accesses_ids)
        user = await self.uow.users.get(request.user_id, eager=True)
        for access in accesses:
            user.accesses.remove(access)

    
    async def reset_group(self, request: ValidatedRequest) -> None:

        group = await self.uow.groups.get(request.group_id, eager=True)
        user = await self.uow.users.get(request.user_id, eager=True)
        
        user.group = group


    async def unset_group(self, request: ValidatedRequest) -> None:

        group = await self.uow.groups.get(request.group_id, eager=True)
        user = await self.uow.users.get(request.user_id, eager=True)
        
        user.group.remove(group)

    
    async def update_request(self, request: ValidatedRequest) -> None:
        if request.validated:
            await self.uow.requests.update_status(request.request_id, "accepted")

        if not request.validated:
            await self.uow.requests.update_status(request.request_id, "denied", request.errors)

    async def _create(self, request: RequestCreate) -> Request:
        request = Request(
            
        )

    


group = await self.uow.groups.get(data.group_id, eager=True)
        accesses = list(group.accesses)

        if data.accesses_id:
            extra_accesses = await self.uow.accesses.get_many(
                data.accesses_id
                )
            accesses.extend(extra_accesses)
        
        user = User(
            name=data.name,
            group=group,
            accesses=accesses,
        )

        await self.uow.users.create(user)
        await self.uow.flush()

        return user