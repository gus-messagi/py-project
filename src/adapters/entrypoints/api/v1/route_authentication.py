import json, bson

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Response, Depends
from fastapi.encoders import jsonable_encoder

from src.domain.dtos.authentication.dto_sign_up import SignUpDto
from src.domain.services.authentication import AuthenticationService
from src.config.container import Container

router = APIRouter()

@router.post("/sign-up")
@inject
def sign_up(
  user: SignUpDto,
  service: AuthenticationService = Depends(Provide[Container.authentication_service])
):
  data = service.sign_up(user=user)
  response = jsonable_encoder(data)

  return Response(
    content=json.dumps(response),
    media_type="application/json",
    status_code=201
  )