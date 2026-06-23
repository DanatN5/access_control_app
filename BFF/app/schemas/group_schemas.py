from pydantic import BaseModel, ConfigDict
from app.schemas.access_schemas import AccessName

class GroupRequestBase(BaseModel):
    id: int
    user_id: int
    action: str
    group_id: int

class GroupRead(BaseModel):
    id: int
    group_name: str
    accesses: list[AccessName]
    forbidden_accesses: list[AccessName]

    model_config = ConfigDict(from_attributes=True)

class GroupName(BaseModel):
    group_name: str

    model_config = ConfigDict(from_attributes=True)
