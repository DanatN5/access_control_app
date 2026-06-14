from typing import Protocol
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User, Access, Group
from app.repositories.repository_protocol import Repository, SQLAlchemyRepo


class GroupRepository(Repository["Group", int],Protocol):
    pass


class GroupSQLAlchemyRepo(SQLAlchemyRepo):
    model = Group
    eager_load_options = [
        selectinload(Group.accesses),
        selectinload(Group.forbidden_accesses),
        selectinload(Group.users)
    ]

 