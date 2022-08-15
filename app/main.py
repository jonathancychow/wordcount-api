import logging
import uvicorn

from app.api.config import config
from app.api.api_v1.api import api_router
from fastapi import FastAPI

logger = logging.getLogger('wordcount')

app = FastAPI()


app.include_router(api_router)
