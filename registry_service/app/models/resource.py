from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.models.access import Access


class Resource(Base):
    __tablename__ = "resources"

    id: Mapped[int] = mapped_column(primary_key=True)
    access: Mapped["Access"] = relationship(
        back_populates="resource",
        uselist=False,
    )