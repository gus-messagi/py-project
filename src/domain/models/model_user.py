from bson import ObjectId
from pydantic import BaseModel, Field
from dataclasses import dataclass

from src.domain.value_objects.vo_object_id import ObjectIdVo

@dataclass
class UserModel(BaseModel):
  id: ObjectIdVo = Field(default_factory=ObjectIdVo, alias='_id')
  name: str
  phone: str
  password: str

  class Config:
    populate_name = True
    arbitrary_types_allowed = True
    json_encoders = {ObjectId: str}