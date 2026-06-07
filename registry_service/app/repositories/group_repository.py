from typing import Protocol
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User, Access, Group


class GroupRepository(Protocol):
    async def get_group_by_id(self, user_id: int) -> User: pass



class GroupSQLAlchemyRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_group_by_id(self, group_id: int) -> Access:
        return await self.session.get(Group, group_id)