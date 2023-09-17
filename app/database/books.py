import uuid

from app.config import config
from app.database import table


def create_book(book_data: dict) -> dict:
    """Creates a new book and auto-generates ID.

    :param book_data: (dict) A dictionary of book info
    :return: (dict) Created book data
    """
    # Create a unique ID for the new book
    if book_data.get("id") is None:
        book_id: str = config.BOOK_ID_FORMAT.format(id=uuid.uuid4())
        book_data["id"] = book_id

    # Commit to DB
    table.put_item(Item=book_data)

    return book_data


def get_book(book_id: str) -> dict:
    """Gets a book from the database using its ID.

    :param book_id: (str) ID of the book
    :return: (dict) Retrieved book data
    """
    response = table.get_item(Key={"id": book_id})
    book = response.get("Item")

    return book
