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


    async def grant_access(self, user_id: int, access_ids: list[int]) -> None:

        accesses = await self.uow.accesses.get(access_ids)
        if len(access_ids) > 1:
            accesses = await self.uow.accesses.get_many(access_ids)
        
        user = await self.uow.users.get(user_id, eager=True)
        user.accesses.append(accesses)

    async def revoke_access(self, user_id: int, access_ids: list[int]) -> None:
        accesses = await self.uow.accesses.get(access_ids)
        if len(access_ids) > 1:
            accesses = await self.uow.accesses.get_many(access_ids)
        user = await self.uow.users.get(user_id, eager=True)
        user.accesses.remove(accesses)

        
    async def reset_group(self, user_id: int, group_id: int) -> None:

        group = await self.uow.groups.get(group_id, eager=True)
        user = await self.uow.users.get(user_id, eager=True)
        
        user.group = group

    async def unset_group(self, user_id: int, group_id: int) -> None:

        group = await self.uow.groups.get(group_id, eager=True)
        user = await self.uow.users.get(user_id, eager=True)
        
        user.group.remove(group)
    