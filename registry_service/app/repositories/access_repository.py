from typing import Protocol
from sqlalchemy import select
from app.models import Access
from app.repositories.repository_protocol import Repository, SQLAlchemyRepo


class AccessRepository(Repository["Access", int], Protocol):
    async def get_many(self, ids: list[int]) -> list[Access]: ...



class AccessSQLAlchemyRepo(SQLAlchemyRepo):
    model = Access
    name = "Access"
    
    async def get_many(self, ids: list[int]) -> list[Access]:
        result = await self.session.scalars(
            select(self.model)
            .where(self.model.id.in_(ids))
        )
        
        return list(result)
