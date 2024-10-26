import json

# import requests


def lambda_handler(event, context):

    print(json.dumps(event))

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "API通信完了",
            # "location": ip.text.replace("\n", "")
        }),
    }
