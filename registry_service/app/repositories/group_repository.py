from typing import Protocol
from sqlalchemy.orm import selectinload
from app.models import Group
from app.repositories.repository_protocol import Repository, SQLAlchemyRepo


class GroupRepository(Repository["Group", int],Protocol):
    pass


class GroupSQLAlchemyRepo(SQLAlchemyRepo):
    model = Group
    name = "Group"
    eager_load_options = [
        selectinload(Group.accesses),
        selectinload(Group.forbidden_accesses),
        selectinload(Group.users)
    ]

 