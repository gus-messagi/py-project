from src.domain.dtos.authentication.dto_sign_up import SignUpDto
from src.domain.ports.repositories.interface_repository_user import UserRepositoryInterface

class AuthenticationService:
  def __init__(self, repository: UserRepositoryInterface) -> None:
    self.repository = repository

  def sign_up(self, user: SignUpDto):
    created_user = self.repository._add(user)

    return SignUpDto(**created_user)