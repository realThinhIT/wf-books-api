import uuid

from app.config import config
from app.database import book_table


def create_book(book_data: dict) -> dict:
    # Create a unique ID for the new book
    if book_data.get("id") is None:
        book_id: str = config.BOOK_ID_FORMAT.format(id=uuid.uuid4())
        book_data["id"] = book_id

    # Commit to DB
    book_table.put_item(Item=book_data)

    return book_data


def get_book(book_id: str) -> dict:
    response = book_table.get_item(Key={"id": book_id})
    book = response.get("Item")

    return book
