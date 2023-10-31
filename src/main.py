from typing import Union
from fastapi import FastAPI
from dotenv import dotenv_values

from src.adapters.entrypoints.api.base import api_router
from src.config.container import Container

config = dotenv_values(".env")

container = Container()
app = FastAPI()

def include_router(_app):
  _app.include_router(api_router, prefix="/v1")

app.container = container

include_router(app)