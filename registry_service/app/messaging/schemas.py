from pydantic import BaseModel
from enum import Enum

class Action(str, Enum):
    GRANT = "grant"
    REVOKE = "revoke"

class RequestValues(BaseModel):
    access_ids: list[int] | None
    group_id: int | None

class RequestMessage(BaseModel):
    request_id: int
    user_id: int
    validated: bool
    action: Action
    values: RequestValues




