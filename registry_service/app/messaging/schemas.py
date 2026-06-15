from pydantic import BaseModel
from enum import Enum

class Action(str, Enum):
    GRANT_ACCESS = "grant access"
    REVOKE_ACCESS = "revoke access"
    RESET_GROUP = "reset group"
    UNSET_GROUP = "unset group"

class RequestMessage(BaseModel):
    request_id: int
    user_id: int
    validated: bool
    action: Action
    target_ids: list[int]



