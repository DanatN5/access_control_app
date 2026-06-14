import enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String
from typing import TYPE_CHECKING
from app.models.associations import group_access, group_forbidden_access
from app.database import Base
if TYPE_CHECKING:
    from app.models.access import Access
    from app.models.user import User


class GroupsEnum(str, enum.Enum):
    DB_ADMIN = 'Database Administrator'
    DEV = 'Developer'
    OWNER = 'Owner'


class Group(Base):
    __tablename__ = "groups"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    group_name: Mapped[GroupsEnum] = mapped_column(String(15), default=GroupsEnum.DEV)
    users: Mapped[list["User"]] = relationship(back_populates="group")
    accesses: Mapped[list["Access"]] = relationship(
        secondary=group_access,
        back_populates="groups"
    )
    forbidden_accesses: Mapped[list["Access"]] = relationship(
        secondary=group_forbidden_access,
        back_populates="forbidden_groups"
    )
