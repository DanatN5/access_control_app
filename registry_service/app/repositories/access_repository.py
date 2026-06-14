from typing import Protocol, TypeVar
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User, Access, Group
from app.repositories.repository_protocol import Repository, SQLAlchemyRepo


class AccessRepository(Repository["Access", int], Protocol):
    async def get_many(self, ids: list[int]) -> list[Access]: ...



class AccessSQLAlchemyRepo(SQLAlchemyRepo):
    model = Access
    
    async def get_many(self, ids: list[int]) -> list[Access]:
        result = await self.session.scalars(
            select(self.model)
            .where(self.model.id.in_(ids))
        )
        
        return list(result)
