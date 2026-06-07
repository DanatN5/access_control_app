from typing import Protocol
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User, Access, Group


class AccessRepository(Protocol):
    async def get_access_by_id(self, user_id: int) -> User: pass



class AccessSQLAlchemyRepo:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_access_by_id(self, access_id: int) -> Access:
        return await self.session.get(Access, access_id)