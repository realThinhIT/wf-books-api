import os

from app.config.base import BaseConfig


class Config(BaseConfig):
    ENVIRONMENT = "test"

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "test")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "test")
    DB_BOOK_TABLE_NAME = os.getenv("DB_DYNAMODB_TABLE", "Books_Test")
    DB_REGION_NAME = os.getenv("DB_REGION_NAME", "ap-southeast-1")
