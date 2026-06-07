from app.repositories.UnitOfWork import UnitOfWork

class UserService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def add_access(self, user_id: int, access_id: int) -> None:
        
        access = await self.uow.accesses.get_access_by_id(access_id)
        await self.uow.users.add_access(user_id, access)

    async def set_group(self, user_id: int, group_id: int) -> None:

        group = await self.uow.groups.get_group_by_id(group_id)
        old_group = await self.uow.users.get_group(user_id)
        if old_group:
            self.uow.users.unset_group
        await self.uow.users.set_group(group)

    