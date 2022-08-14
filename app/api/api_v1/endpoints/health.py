import logging
from fastapi import APIRouter

logger = logging.getLogger('wordcount')

router = APIRouter()

@router.get("/")
def GetModel():
    return {
        "name": "wordcountingservice",
        "status": "ok",
        "version": "1.0.0"
    }
