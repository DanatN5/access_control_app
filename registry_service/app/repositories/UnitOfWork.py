from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.access_repository import AccessSQLAlchemyRepo
from app.repositories.group_repository import GroupSQLAlchemyRepo
from app.repositories.user_repository import UserSQLAlchemyRepo


class UnitOfWork:
    def __init__(self, session: AsyncSession):
        self.sesson = session

    async def __aenter__(self):

        self.users = UserSQLAlchemyRepo(self.session)
        self.accesses = AccessSQLAlchemyRepo(self.session)
        self.groups = GroupSQLAlchemyRepo(self.session)

        return self
    
    async def __aexit__(self, exc_type, exc, tb):

        if exc_type:
            await self.session.rollback()
        else:
            await self.session.commit()
    


    


        