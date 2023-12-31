import os
import uuid

import boto3
import moto
import pytest
from fastapi.testclient import TestClient

from app.config import config
from app.main import app
from tests.utils import generate_random_str

table_name = config.DB_DYNAMODB_TABLE
key_schema = [
    {
        "AttributeName": "id",
        "KeyType": "HASH",
    },
]
attributes_definition = [
    {"AttributeName": "id", "AttributeType": "S"},
]
provisioned_throughput = {
    "ReadCapacityUnits": 5,
    "WriteCapacityUnits": 5,
}


@pytest.fixture(scope="session", autouse=True)
def check_env_and_create_table(*_, **__):
    from app.database import dynamodb, dynamodb_client

    # Only allow running tests in test environment
    if os.getenv("ENV") != "test":
        raise Exception("Tests can only be executed in 'test' environment.")

    # For integration tests: If test table is not available, create one
    if config.DB_DYNAMODB_TABLE not in [table.name for table in dynamodb.tables.all()]:
        dynamodb.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attributes_definition,
            ProvisionedThroughput=provisioned_throughput
        )

        waiter = dynamodb_client.get_waiter('table_exists')  # Wait till the table is created
        waiter.wait(TableName=config.DB_DYNAMODB_TABLE)

    # Check if the test table is available
    assert config.DB_DYNAMODB_TABLE in [table.name for table in dynamodb.tables.all()]


@pytest.fixture
@moto.mock_dynamodb
def app_client():
    """
    Create a FastAPI test client fixture.
    """

    return TestClient(app)


def create_mock_book_table():
    # Create table
    dynamodb = boto3.client(
        "dynamodb",
        aws_access_key_id="test",
        aws_secret_access_key="test",
        region_name=config.DB_REGION_NAME
    )

    dynamodb.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attributes_definition,
        ProvisionedThroughput=provisioned_throughput
    )

    tables = dynamodb.list_tables()["TableNames"]
    assert table_name in tables

    return boto3.resource(
        "dynamodb",
        aws_access_key_id="test",
        aws_secret_access_key="test",
        region_name=config.DB_REGION_NAME
    ).Table(table_name)


def generate_dummy_book_data():
    return {
        "author": config.AUTHOR_ID_FORMAT.format(id=uuid.uuid4()),
        "name": generate_random_str(100),
        "note": generate_random_str(100),
        "serial": generate_random_str(100)
    }
