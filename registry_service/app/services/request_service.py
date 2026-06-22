from app.repositories.uow import UnitOfWork
from app.schemas.request_schemas import ValidatedRequest, RequestStatus
from app.models import Request

class RequestService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow
        self.cases = {
            "grant access": self.grant_access,
            "revoke access": self.revoke_access,
            "reset group": self.reset_group,
            "unset group": self.unset_group,
        }

    
    async def process_request(self, request: ValidatedRequest) -> None:
        
        if request.validated:
            await self.cases[request.action](request)
        
        await self._create(request)


    async def grant_access(self, request: ValidatedRequest) -> None:
        accesses = await self.uow.accesses.get_many(request.accesses_ids)
        user = await self.uow.users.get(request.user_id, eager=True)
        user.accesses.extend(accesses)

    
    async def revoke_access(self, request: ValidatedRequest) -> None:

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


    async def _create(self, request: ValidatedRequest) -> Request:

        if request.validated:
            status = RequestStatus.ACCEPTED
        
        if not request.validated:
            status = RequestStatus.DENIED

        request = Request(
            user_id=request.user_id,
            group_id=request.group_id,
            action=request.action,
            accesses_ids=request.accesses_ids,
            status=status
        )
        await self.uow.requests.create(request)
        await self.uow.flush()

        return request
