from pydantic import BaseModel
from enum import Enum

class Action(str, Enum):
    GRANT_ACCESS = "grant access"
    REVOKE_ACCESS = "revoke access"
    RESET_GROUP = "reset group"
    UNSET_GROUP = "unset group"

class Status(str, Enum):
    PENDING = "pending"
    DENIED = "denied"
    ACCEPTED = "accepted"

class RequestBase(BaseModel):
    request_id: int
    stasus: Status
    user_id: int
    action: Action
    accesses_ids: list[int] | None
    group_id: int | None

class RequestCreate(BaseModel):
    stasus: Status
    user_id: int
    action: Action
    accesses_ids: list[int] | None
    group_id: int | None

class ValidatedRequest(BaseModel):
    request_id: int
    validated: bool
    errors: list[str] = []
    user_id: int
    action: Action
    accesses_ids: list[int] | None
    group_id: int | None


class RequestStatus(BaseModel):
    status: Status