from pydantic import BaseModel, Field

class GroupRequest(BaseModel):
    id: int
    user_id: int
    action: str
    group_id: int


class AccessRequest(BaseModel):
    id: int
    user_id: int
    action: str
    access_id: int
