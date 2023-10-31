import json

from src.domain.ports.repositories.interface_repository_user import UserRepositoryInterface
from src.domain.dtos.authentication.dto_sign_up import SignUpDto
from src.config.database import user_collection

class UserRepository(UserRepositoryInterface):
  def __init__(self):
    super().__init__()
    self.collection = user_collection

  def _add(self, user):
    result = self.collection.insert_one(dict(user))
    assert result.acknowledged

    id = result.inserted_id

    return self.collection.find_one({ "_id": id })
