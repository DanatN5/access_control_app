from app.models.associations import user_accesses
from app.models.group import Group
from app.models.access import Access
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(15))
    accesses: Mapped[list["Access"]] = relationship(
        secondary=user_accesses,
        back_populates="users"
    )
    group_id: Mapped[int | None] = mapped_column(ForeignKey("groups.id"), nullable=True)
    group: Mapped["Group | None"] = relationship(back_populates="users")