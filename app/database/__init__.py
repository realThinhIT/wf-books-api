import boto3

from app.config import config

dynamodb = boto3.resource("dynamodb", region_name=config.DB_REGION_NAME)
dynamodb_client = boto3.client("dynamodb", region_name=config.DB_REGION_NAME)

table = dynamodb.Table(config.DB_DYNAMODB_TABLE)
