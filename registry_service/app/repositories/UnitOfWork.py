from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.access_repository import AccessSQLAlchemyRepo
from app.repositories.group_repository import GroupSQLAlchemyRepo
from app.repositories.user_repository import UserSQLAlchemyRepo
from typing import Protocol


class UnitOfWork(Protocol):
    async def __aenter__(self): pass

    async def __aexit__(self, exc_type, exc, tb): pass

    async def commit(self): pass

    async def rollback(self): pass
    

class SQLAlchemyUnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repositories = {}

    async def __aenter__(self):

        self.users = UserSQLAlchemyRepo(self.session)
        self.accesses = AccessSQLAlchemyRepo(self.session)
        self.groups = GroupSQLAlchemyRepo(self.session)

        return self
    
    async def __aexit__(self, exc_type, exc, tb):

        if exc_type:
            await self.rollback()
        else:
            await self.commit()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
    


    


        