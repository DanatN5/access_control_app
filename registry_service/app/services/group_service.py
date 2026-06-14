from app.repositories.uow import UnitOfWork
from app.schemas.group_schemas import GroupCreate, GroupRead
from app.models.group import Group
from sqlalchemy.ext.asyncio import AsyncSession

class GroupService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_group(self, data: GroupCreate) -> Group:
        accesses = []
        forbidden_accesses = []
        if data.access_ids:
            accesses = await self.uow.accesses.get_many(
                data.access_ids
            )
        if data.forbidden_access_ids:
            forbidden_accesses = await self.uow.accesses.get_many(
                data.forbidden_access_ids
            )
        group = Group(
            group_name=data.group_name,
            accesses=accesses,
            forbidden_accesses=forbidden_accesses
        )
        
        await self.uow.groups.create(group)
        await self.uow.flush()

        return group       

