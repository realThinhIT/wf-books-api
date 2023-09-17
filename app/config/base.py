import os


class BaseConfig:
    ENV = None

    DB_DYNAMODB_TABLE = os.getenv("DB_DYNAMODB_TABLE", "Books-dev")
    DB_REGION_NAME = os.getenv("DB_REGION_NAME", "ap-southeast-1")

    BOOK_ID_FORMAT = "/books/{id}"
    AUTHOR_ID_FORMAT = "/authors/{id}"
