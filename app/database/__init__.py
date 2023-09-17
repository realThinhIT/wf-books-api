import boto3

from app.config import config

dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
    region_name=config.DB_REGION_NAME
)

table = dynamodb.Table(config.DB_DYNAMODB_TABLE)
