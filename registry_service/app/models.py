from sqlalchemy import Integer, String, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(15))
    accessses: Mapped[list["Access"]] = mapped_column()
    groups: Mapped[list["Group"]] = mapped_column()

class Resource(Base):
    __tablename__ = "resources"

    id: Mapped[int] = mapped_column(primary_key=True)
    access: Mapped["Access"] = relationship(
        back_populates="resource",
        uselist=False,
    )
    
group_access = Table(
    "group_access",
    Base.metadata,
    Column("group_id", ForeignKey("groups.id"), primary_key=True),
    Column("access_id", ForeignKey("accesses.id"), primary_key=True)

)
class Access(Base):
    __tablename__ = "accesses"

    id: Mapped[int] = mapped_column(primary_key=True)
    resourse_id: Mapped[int] = mapped_column(
        ForeignKey("resource.id"),
        unique=True,
        )
    resourse: Mapped["Resource"] = relationship(back_populates="access")
    groups: Mapped[list["Group"]] = relationship(
        secondary=group_access,
        back_populates="accesses"
    )

class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    group_name: Mapped[str] = mapped_column(String(15))
    accesses: Mapped[list["Access"]] = relationship(
        secondary=group_access,
        back_populates="groups"
    )


