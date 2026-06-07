from sqlalchemy import Integer, String, ForeignKey, Table, Column, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship


import enum

from app.database import Base

user_accesses = Table(
    "user_accesses",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("access_id", ForeignKey("accesses.id"), primary_key=True)
)

    
group_access = Table(
    "group_access",
    Base.metadata,
    Column("group_id", ForeignKey("groups.id"), primary_key=True),
    Column("access_id", ForeignKey("accesses.id"), primary_key=True)
)
group_forbidden_access = Table(
    "group_forbidden_access",
    Base.metadata,
    Column("group_id", ForeignKey("groups.id"), primary_key=True),
    Column("access_id", ForeignKey("accesses.id"), primary_key=True)
)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(15))
    accesses: Mapped[list["Access"]] = relationship(
        secondary=user_accesses,
        back_populates="users"
    )
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    group: Mapped["Group"] = relationship(back_populates="users")

class Resource(Base):
    __tablename__ = "resources"

    id: Mapped[int] = mapped_column(primary_key=True)
    access: Mapped["Access"] = relationship(
        back_populates="resource",
        uselist=False,
    )

class GroupsEnum(str, enum.Enum):
    DB_ADMIN = 'Database Administrator'
    DEV = 'Developer'
    OWNER = 'Owner'

class Access(Base):
    __tablename__ = "accesses"

    id: Mapped[int] = mapped_column(primary_key=True)
    access_name: Mapped[str] = mapped_column(String(20))
    resourse_id: Mapped[int] = mapped_column(
        ForeignKey("resource.id"),
        unique=True,
        )
    resourse: Mapped["Resource"] = relationship(back_populates="access")
    credentials: Mapped[dict] = mapped_column(JSON)
    
    groups: Mapped[list["Group"]] = relationship(
        secondary=group_access,
        back_populates="accesses"
    )
    forbidden_groups: Mapped[list["Group"]] = relationship(
        secondary=group_forbidden_access,
        back_populates="forbidden_accesses"
    )

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


