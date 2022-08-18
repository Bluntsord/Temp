import boto3

s3_client = boto3.resource("s3")
bucket_name = 'dev-snowflake-s3'
bucket = s3_client.Bucket(bucket_name)


def print_hello(event, context):
    for obj in bucket.objects.all():
        print(obj.key, obj.last_modified)
    return {