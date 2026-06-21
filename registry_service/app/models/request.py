from app.database import Base
from sqlalchemy import DateTime, func, JSON
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum
from datetime import datetime


class RequestStatus(str, Enum):
    pending = "PENDING"
    accepted = "ACCEPTED"
    denied = "DENIED"

class Action(str, Enum):
    GRANT_ACCESS = "grant access"
    REVOKE_ACCESS = "revoke access"
    RESET_GROUP = "reset group"
    UNSET_GROUP = "unset group"


class Request(Base):
    __tablename__ = "requests"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[RequestStatus]
    user_id: Mapped[int]
    action: Mapped[Action]
    accesses_ids: Mapped[list[int] | None] = mapped_column(JSON, nullable=True)
    group_id: Mapped[int | None] = mapped_column(nullable=True)
    errors: Mapped[list[int] | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now()
        )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
        )

    def to_dict(self) -> dict:
        result = {}
        for col in self.__table__.columns:
            value = getattr(self, col.name)
            if isinstance(value, datetime):
                value = value.isoformat()
            result[col.name] = value
        return result

