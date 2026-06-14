from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from app.models.associations import group_access, group_forbidden_access, user_accesses
from app.database import Base
if TYPE_CHECKING:
    from app.models.group import Group
    from app.models.user import User



class Access(Base):
    __tablename__ = "accesses"

    id: Mapped[int] = mapped_column(primary_key=True)
    access_name: Mapped[str] = mapped_column(String(20))
    resource_name: Mapped[str] = mapped_column(String(20), unique=True)
    credentials: Mapped[dict] = mapped_column(JSON)

    users: Mapped[list["User"]] = relationship(
        secondary=user_accesses,
        back_populates="accesses"
    )
    
    groups: Mapped[list["Group"]] = relationship(
        secondary=group_access,
        back_populates="accesses"
    )
    forbidden_groups: Mapped[list["Group"]] = relationship(
        secondary=group_forbidden_access,
        back_populates="forbidden_accesses"
    )