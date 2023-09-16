from fastapi import APIRouter

RESOURCE_PREFIX = "/books"
router = APIRouter(
    prefix=RESOURCE_PREFIX
)


@router.get("/")
async def get_all_books():
    return []


@router.get("/{book_id}")
async def get_book(book_id: int):
    return {}
