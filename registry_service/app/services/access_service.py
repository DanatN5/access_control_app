from app.repositories.uow import UnitOfWork
from app.schemas.access_schemas import AccessCreate, AccessRead
from app.models.access import Access
from sqlalchemy.ext.asyncio import AsyncSession

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