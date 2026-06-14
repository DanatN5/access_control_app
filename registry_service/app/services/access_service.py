from app.repositories.uow import UnitOfWork
from app.schemas.access_schemas import AccessCreate
from app.models.access import Access

class AccessService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_access(self, data: AccessCreate) -> Access:
        access = Access(
            access_name=data.access_name,
            resource_name=data.resource_name,
            credentials=data.credentials
        )
        
        await self.uow.accesses.create(access)
        await self.uow.flush()

        return access       