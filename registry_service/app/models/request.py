from app.database import Base
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum
from datetime import datetime


class RequestStatus(str, Enum):
    pending = "PENDING"
    accepted = "ACCEPTED"
    denied = "DENIED"


class Request(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[RequestStatus]
    created_at: Mapped[datetime] = mapped_column(DateTime)
    updated_at: Mapped[datetime] = mapped_column(DateTime)

    def to_dict(self) -> dict:
        result = {}
        for col in self.__table__.columns:
            value = getattr(self, col.name)
            if isinstance(value, datetime):
                value = value.isoformat()
            result[col.name] = value
        return result

