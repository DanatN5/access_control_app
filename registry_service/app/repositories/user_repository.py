from typing import Protocol
from sqlalchemy.orm import selectinload
from app.repositories.repository_protocol import Repository, SQLAlchemyRepo
from app.models import User


class UserRepository(Repository["User", int], Protocol):
    pass
    

class UserSQLAlchemyRepo(SQLAlchemyRepo):
    model = User
    eager_load_options = [
        selectinload(User.accesses),
        selectinload(User.group)
    ]





