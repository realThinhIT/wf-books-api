import os

from app.config.base import BaseConfig


class Config(BaseConfig):
    ENV = "test"

    DB_DYNAMODB_TABLE = os.getenv("DB_DYNAMODB_TABLE", "Books-test")
    DB_REGION_NAME = os.getenv("DB_REGION_NAME", "ap-southeast-1")
