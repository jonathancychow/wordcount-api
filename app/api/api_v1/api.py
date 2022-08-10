from fastapi import APIRouter
from .endpoints import health, count

api_router = APIRouter()

api_router.include_router(count.router, prefix="/count", tags=["Count"])
api_router.include_router(health.router, prefix="/health", tags=["Health"])
