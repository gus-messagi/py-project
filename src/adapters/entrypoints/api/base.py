import json

from fastapi import APIRouter, Response

from src.adapters.entrypoints.api.v1 import (
  route_authentication
)

api_router = APIRouter()
api_router.include_router(route_authentication.router, prefix="/authentication", tags=["authentication"])

@api_router.get("/")
def get_version():
  return Response(
    content=json.dumps({
      "version": "v1"
    }),
    media_type="application/json",
    status_code=200
  )