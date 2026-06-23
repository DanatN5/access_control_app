from pydantic import BaseModel
from enum import Enum
from app.models.request import Action, RequestStatus

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


class ValidatedRequest(BaseModel):
  
    validated: bool
    errors: str | None
    user_id: int
    action: Action
    accesses_ids: list[int] | None
    group_id: int | None
