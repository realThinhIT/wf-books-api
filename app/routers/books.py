from typing import List, Any

from fastapi import APIRouter

from app.schemas.books import BookOut

RESOURCE_PREFIX = "/books"
router = APIRouter(
    prefix=RESOURCE_PREFIX,
    tags=["Books"]
)


@router.get(
    "/",
    response_model=List[BookOut]
)
async def get_all_books() -> Any:
    return []


@router.get(
    "/{book_id}",
    response_model=BookOut
)
async def get_book(book_id: int) -> Any:
    return {}
