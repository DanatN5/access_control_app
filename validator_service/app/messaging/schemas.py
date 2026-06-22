from pydantic import BaseModel
from enum import Enum

class Action(str, Enum):
    GRANT_ACCESS = "grant access"
    REVOKE_ACCESS = "revoke access"
    RESET_GROUP = "reset group"
    UNSET_GROUP = "unset group"

class Request(BaseModel):
    user_id: int
    action: Action
    accesses_ids: list[int] | None
    group_id: int | None

class RequestValidatedEvent(BaseModel):
    validated: bool
    errors: list[str] = []
    user_id: int
    action: Action
    accesses_ids: list[int] | None
    group_id: int | None


class AccessNameInfo(BaseModel):
    access_name: str


class AccessInfo(BaseModel):
    id: int
    access_name: str
    resource_name: str


class GroupInfo(BaseModel):
    id: int
    group_name: str
    accesses: list[AccessNameInfo]
    forbidden_accesses: list[AccessNameInfo]

