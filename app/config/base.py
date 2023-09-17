import os


class BaseConfig:
    ENVIRONMENT = None

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    DB_DYNAMODB_TABLE = os.getenv("DB_DYNAMODB_TABLE", "Books")
    DB_REGION_NAME = os.getenv("DB_REGION_NAME", "ap-southeast-1")

    BOOK_ID_FORMAT = "/books/{id}"
    AUTHOR_ID_FORMAT = "/authors/{id}"