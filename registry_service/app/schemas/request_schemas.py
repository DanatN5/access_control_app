from pydantic import BaseModel
from enum import Enum
from app.models.request import Action, RequestStatus

class RequestRead(BaseModel):
    id: int
    status: RequestStatus
    user_id: int
    action: Action
    accesses_ids: list[int] | None
    group_id: int | None

class RequestReadShort(BaseModel):
    id: int
    status: RequestStatus


class RequestCreate(BaseModel):
    user_id: int
    action: Action
    accesses_ids: list[int] | None
    group_id: int | None

class ValidatedRequest(BaseModel):
    id: int
    validated: bool
    errors: list[str] = []
    user_id: int
    action: Action
    accesses_ids: list[int] | None
    group_id: int | None
