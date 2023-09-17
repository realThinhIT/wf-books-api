import moto

from app.database import books as book_db
from tests.conftest import create_book_table, generate_dummy_book_data
from tests.utils import batch_assert


@moto.mock_dynamodb
def test_create_book_func_success():
    # Create book table
    resource = create_book_table()

    # Try to create book
    book_data = book_db.create_book(generate_dummy_book_data())

    # Check if the newly created book is in the DB
    newly_created_book = resource.get_item(
        Key={"id": book_data["id"]}
    ).get('Item')

    # Assert data between created book and queried one
    assert newly_created_book is not None
    batch_assert(newly_created_book, book_data, ["id", "author", "name", "note", "serial"])


@moto.mock_dynamodb
def test_get_book_func_success():
    # Create book table and populate a new book
    create_book_table()
    book_data = generate_dummy_book_data()
    book_db.create_book(book_data)

    # Get book
    retrieved_book = book_db.get_book(book_data["id"])

    # Assert data between created book and retrieved one
    assert retrieved_book is not None
    batch_assert(retrieved_book, book_data, ["id", "author", "name", "note", "serial"])
