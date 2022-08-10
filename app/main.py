import logging
import uvicorn

from app.api.config import config
from app.api.api_v1.api import api_router
from fastapi import FastAPI

logger = logging.getLogger('wordcount')

app = FastAPI()

@app.get("/")
def read_root():
    return 'Server is running'

app.include_router(api_router)
