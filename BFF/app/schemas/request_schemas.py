from pydantic import BaseModel
from enum import Enum

class Action(str, Enum):
    GRANT_ACCESS = "grant access"
    REVOKE_ACCESS = "revoke access"
    RESET_GROUP = "reset group"
    UNSET_GROUP = "unset group"

class RequestStatus(str, Enum):
    PENDING = "pending"
    DENIED = "denied"
    ACCEPTED = "accepted"

class RequestCreate(BaseModel):
    user_id: int
    action: Action
    accesses_ids: list[int] | None
    group_id: int | None

class RequestRead(BaseModel):
    id: int
    status: RequestStatus
    errors: str | None
    user_id: int
    action: Action
    accesses_ids: list[int] | None
    group_id: int | None

class RequestReadShort(BaseModel):
    id: int
    status: RequestStatus
    errors: str | None