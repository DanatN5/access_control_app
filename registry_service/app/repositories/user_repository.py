from typing import Protocol
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from app.repositories.repository_protocol import Repository, SQLAlchemyRepo
from app.models import User
from app.models import Access
from app.models import Group


class UserRepository(Repository["User", int], Protocol):
    pass
    
    # async def add_access(self, user_id: int, access: Access) -> None: pass

    # async def get_accesses(self, user_id)

    # async def set_group(self, group: Group) -> None: pass

    # async def get_group(self, user_id: int) -> Group | None: pass

    # async def revoke_access(self, access: Access) -> None: pass

    # async def unset_group(self, group: Group) -> None: pass


class UserSQLAlchemyRepo(SQLAlchemyRepo):
    model = User
    eager_load_options = [
        selectinload(User.accesses),
        selectinload(User.group)
    ]
    # def __init__(self, session: AsyncSession):
    #     self.session = session
    
    # async def get(self, user_id: int) -> User:
    #     return await self.session.get(User, user_id)
    
    # async def add_access(self, user_id: int, access: Access) -> None:
    #     user = await self.session.get(User, user_id)
    #     user.accesses.append(access)
        

    # async def set_group(self, user_id: int, group: Group) -> None:
    #     user = await self.session.get(User, user_id)
    #     user.group.append(group)

    # async def get_group(self, user_id: int) -> Group | None:
    #     user = await self.session.get(User, user_id)
    #     if user.group:
    #         return user.group
    #     return None

    # async def revoke_access(self, user_id: int, access: Access) -> None:
    #     user = await self.session.get(User, user_id)
    #     user.accesses.remove(access)


    # async def unset_group(self, user_id: int, group: Group) -> None:
    #     user = await self.session.get(User, user_id)
    #     user.group.remove(group)





