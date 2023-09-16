from fastapi import APIRouter

RESOURCE_PREFIX = "/authors"
router = APIRouter(
    prefix=RESOURCE_PREFIX
)


@router.get("/")
async def get_all_authors():
    return []


@router.get("/{author_id}")
async def get_author(author_id: int):
    return {}
