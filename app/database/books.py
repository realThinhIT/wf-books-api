import uuid

from app.database import book_table

BOOK_ID_FORMAT = "/books/{id}"

def create_book(book_data: dict):
    # Create an unique ID for the new book
    if book_data.get("id") is None:
        book_id: str = BOOK_ID_FORMAT.format(id=uuid.uuid4())
        book_data["id"] = book_id

    book_table.put_item(Item=book_data)

    return book_data


def get_book(book_id: str):
    response = book_table.get_item(Key={"id": BOOK_ID_FORMAT.format(id=book_id)})
    book = response.get("Item")

    return book
