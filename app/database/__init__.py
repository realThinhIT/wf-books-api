import boto3

dynamodb = boto3.resource(
    "dynamodb",
    region_name="ap-southeast-1"
)
