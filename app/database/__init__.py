import os

import boto3

dynamodb = boto3.resource(
    "dynamodb",
    region_name="ap-southeast-1"
)

book_table = dynamodb.Table(os.getenv("DB_BOOK_TABLE_NAME", "Books"))
