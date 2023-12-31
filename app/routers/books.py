from typing import Any

from botocore.exceptions import ClientError
from fastapi import APIRouter, HTTPException, status

from app.config import config
from app.schemas.books import BookOut, BookIn
from app.database import books as book_db

RESOURCE_PREFIX = "/books"
router = APIRouter(
    prefix=RESOURCE_PREFIX,
    tags=["Books"]
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=BookOut
)
async def create_book(book_data: BookIn) -> Any:
    # Create a new book in DB, raise errors if any
    try:
        new_book = book_db.create_book(book_data.dict())
    except (ClientError, Exception) as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

    return new_book


@router.get(
    "/{book_id}",
    response_model=BookOut
)
async def get_book(book_id: str) -> Any:
    # Retrieve book from the DB, raise errors if any
    try:
        book = book_db.get_book(config.BOOK_ID_FORMAT.format(id=book_id))
    except (ClientError, Exception) as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

    if not book:
        raise HTTPException(status_code=404, detail=f"Could not find book with ID {book_id}")

    return book
