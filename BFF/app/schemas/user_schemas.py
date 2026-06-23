from pydantic import BaseModel, Field, ConfigDict
from app.schemas.access_schemas import AccessName
from app.schemas.group_schemas import GroupName



class UserRead(BaseModel):
    id: int
    name: str
    group: GroupName | None
    accesses: list[AccessName]

    model_config = ConfigDict(from_attributes=True)

class UserName(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)
