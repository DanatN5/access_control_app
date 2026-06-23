from pydantic import BaseModel, ConfigDict, Field

class AccessRequestBase(BaseModel):
    id: int
    user_id: int
    action: str
    access_id: int


class AccessCreate(BaseModel):
    access_name: str = Field(max_length=20)
    resource_name: str = Field(max_length=20)
    credentials: dict


class AccessRead(BaseModel):
    id: int
    access_name: str
    resource_name: str

    model_config = ConfigDict(from_attributes=True)


class AccessName(BaseModel):
    access_name: str

    model_config = ConfigDict(from_attributes=True)