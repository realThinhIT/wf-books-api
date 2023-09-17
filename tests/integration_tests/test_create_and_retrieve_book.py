from fastapi import status

from tests.conftest import generate_dummy_book_data
from tests.utils import batch_assert


def test_create_and_retrieve_book(app_client):
    # Call API to commit to create a new record in external test DB
    new_book_data = generate_dummy_book_data()
    create_response = app_client.post(
        "/api/books",
        json=new_book_data
    )

    # Assert HTTP Code = 201 Created
    assert create_response.status_code == status.HTTP_201_CREATED

    # Assert JSON values
    batch_assert(new_book_data, create_response.json(), ["author", "name", "note", "serial"])
    assert create_response.json()["id"] is not None  # new ID is generated

    # Perform a GET request to get the newly created record
    raw_book_id = create_response.json()['id'].replace('/books/', '')
    get_response = app_client.get(
        f"/api/books/{raw_book_id}"
    )

    # Assert HTTP Code = 200 OK
    assert get_response.status_code == status.HTTP_200_OK

    # Assert JSON values
    batch_assert(new_book_data, get_response.json(), ["author", "name", "note", "serial"])
    assert get_response.json()["id"] == create_response.json()["id"]
