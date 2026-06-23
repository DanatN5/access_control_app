from pydantic import BaseModel, ConfigDict

class AccessRequestBase(BaseModel):
    id: int
    user_id: int
    action: str
    access_id: int

class AccessRead(BaseModel):
    id: int
    access_name: str
    resource_name: str

    model_config = ConfigDict(from_attributes=True)

class AccessName(BaseModel):
    access_name: str

    model_config = ConfigDict(from_attributes=True)