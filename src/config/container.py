from dotenv import dotenv_values
from dependency_injector import containers, providers
from pymongo import MongoClient

from src.adapters.repositories import (
  repository_user
)

from src.domain.services import (
  authentication
)

config = dotenv_values(".env")

class Container(containers.DeclarativeContainer):
  wiring_config = containers.WiringConfiguration(
    packages=[
      "src.adapters.entrypoints.api.v1"
    ]
  )

  user_repository = providers.ThreadSafeSingleton(
    repository_user.UserRepository,
  )

  authentication_service = providers.Factory(
    authentication.AuthenticationService,
    repository= user_repository
  )