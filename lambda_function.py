import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps("CI/CD Pipeline Working and this is night 2:20")
    }