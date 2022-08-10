import logging
from fastapi import APIRouter

logger = logging.getLogger('wordcount')

router = APIRouter()

@router.get("/")
def GetModel():
    return 'Server is running'
