from typing import Protocol, TypeVar, Generic
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption
from sqlalchemy import select
from app.exceptions.exceptions import NotFoundError

T = TypeVar("T")
ID = TypeVar("ID")

class Repository(Protocol, Generic[T, ID]):
    async def get(self, id: ID, options: list | None = None) -> T: pass

    async def create(self, entity: T) -> T: pass

    async def delete(self, id: ID) -> None: pass

    async def list(self, options: list | None = None) -> list[T]: pass


class SQLAlchemyRepo(Generic[T, ID]):

    model: type[T]
    name: str
    eager_load_options: list[ExecutableOption] | None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, id: ID, eager: bool = False) -> T | None:
        stmt = select(self.model).where(
            self.model.id == id
            )
        
        if eager:
            stmt = stmt.options(*self.eager_load_options)
        result =  await self.session.scalar(stmt)

        if result is None:
            raise NotFoundError(id, self.name)
        
        return result

    
    async def create(self, entity: T) -> T:
        self.session.add(entity)
        return entity
    
    async def delete(self, id: T) -> None:
        entity = await self.get(id)
        await self.session.delete(entity)

    async def list(self, eager: bool = False) -> list[T]:
        stmt = select(self.model)
        if eager:
            stmt = stmt.options(*self.eager_load_options)
        result = await self.session.scalars(stmt)

        return list(result)
        