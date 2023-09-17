import moto
from starlette import status

from app.database import books as book_db
from tests.conftest import generate_dummy_book_data, create_book_table
from tests.utils import batch_assert, generate_random_str


@moto.mock_dynamodb
def test_create_book_api_success(app_client):
    # Create book table
    create_book_table()

    # Send a POST request to create a new book
    new_book_data = generate_dummy_book_data()

    response = app_client.post(
        "/api/books",
        json=new_book_data
    )

    # Assert HTTP Code = 201 Created
    assert response.status_code == status.HTTP_201_CREATED

    # Assert JSON values
    batch_assert(new_book_data, response.json(), ["author", "name", "note", "serial"])
    assert response.json()["id"] is not None  # new ID is generated


@moto.mock_dynamodb
def test_create_book_api_failed_400(app_client):
    # Create book table
    create_book_table()

    # Send a POST request to create a new book
    new_book_data = generate_dummy_book_data()

    # Wrong author format
    response1 = app_client.post(
        "/api/books",
        json={
            **new_book_data,
            "author": "not-a-valid-author-id"
        }
    )
    assert response1.status_code == status.HTTP_400_BAD_REQUEST

    # Name is invalid
    response2 = app_client.post(
        "/api/books",
        json={
            **new_book_data,
            "name": None
        }
    )
    assert response2.status_code == status.HTTP_400_BAD_REQUEST


@moto.mock_dynamodb
def test_create_book_api_failed_500(app_client):
    # Not init book table so Boto would raise Exception

    # Send a POST request to create a new book
    new_book_data = generate_dummy_book_data()

    # Wrong author format
    response1 = app_client.post(
        "/api/books",
        json=new_book_data
    )
    assert response1.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR


@moto.mock_dynamodb
def test_get_book_api_success(app_client):
    # Create book table and create a new book in the DB
    create_book_table()
    new_book_data = book_db.create_book(generate_dummy_book_data())

    # Perform a GET request to get the record
    raw_book_id = new_book_data['id'].replace('/books/', '')
    response = app_client.get(
        f"/api/books/{raw_book_id}"
    )

    # Assert HTTP Code = 200 OK
    assert response.status_code == status.HTTP_200_OK

    # Assert JSON values
    batch_assert(new_book_data, response.json(), ["id", "author", "name", "note", "serial"])


@moto.mock_dynamodb
def test_get_book_api_failed_404(app_client):
    # Create book table and create a new book in the DB
    create_book_table()

    # Perform a GET request to get the record
    response = app_client.get(
        f"/api/books/{generate_random_str(50)}"
    )

    # Assert HTTP Code = 404 Not Found
    assert response.status_code == status.HTTP_404_NOT_FOUND


@moto.mock_dynamodb
def test_get_book_api_failed_500(app_client):
    # Not init book table so Boto would raise Exception
    # Perform a GET request to get the record
    response = app_client.get(
        f"/api/books/{generate_random_str(50)}"
    )

    # Assert HTTP Code = 500 Internal Server Error
    assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
