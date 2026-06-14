from app.repositories.uow import UnitOfWork
from app.schemas.user_schemas import UserCreate
from app.models import User, Group, Access

class UserService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create(
            self,
            data: UserCreate
    ) -> User:
    
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
    
    
    async def get_group(self, user_id: int) -> Group:
        user = await self.uow.users.get(user_id, eager=True)
        group = await self.uow.groups.get(user.group.id, eager=True)

        return group
    
    async def get_accesses(self, user_id: int) -> list[Access]:
        user = await self.uow.users.get(user_id, eager=True)
        acceses_ids = [access.id for access in user.accesses]
        user_accesses = await self.uow.accesses.get_many(acceses_ids)

        return user_accesses



    async def add_access(self, user_id: int, access_id: int) -> None:
        
        access = await self.uow.accesses.get(access_id)
        user = await self.uow.users.get(user_id)
        user.accesses.append(access)
        

    async def set_group(self, user_id: int, group_id: int) -> None:

        group = await self.uow.groups.get_group_by_id(group_id)
        old_group = await self.uow.users.get_group(user_id)
        if old_group:
            self.uow.users.unset_group
        await self.uow.users.set_group(group)

    