from fastapi import APIRouter

from app.routers.books import router as books_router

# Append /api prefix for all existing APIs
api_routers = APIRouter(prefix="/api")
api_routers.include_router(books_router)
