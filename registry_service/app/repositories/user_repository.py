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
    

class UserSQLAlchemyRepo(SQLAlchemyRepo):
    model = User
    eager_load_options = [
        selectinload(User.accesses),
        selectinload(User.group)
    ]





