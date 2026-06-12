from sqlalchemy import ForeignKey, String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.models.resource import Resource
from app.models.group import Group
from app.models.associations import group_access, group_forbidden_access




class Access(Base):
    __tablename__ = "accesses"

    id: Mapped[int] = mapped_column(primary_key=True)
    access_name: Mapped[str] = mapped_column(String(20))
    resourse_id: Mapped[int] = mapped_column(
        ForeignKey("resource.id"),
        unique=True,
        )
    resource: Mapped["Resource"] = relationship(back_populates="access")
    credentials: Mapped[dict] = mapped_column(JSON)
    
    groups: Mapped[list["Group"]] = relationship(
        secondary=group_access,
        back_populates="accesses"
    )
    forbidden_groups: Mapped[list["Group"]] = relationship(
        secondary=group_forbidden_access,
        back_populates="forbidden_accesses"
    )