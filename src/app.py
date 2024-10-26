import json
import requests

url = "https://api.line.me/oauth2/v2.1/verify"

def lambda_handler(event, context):

    print(json.dumps(event))

    idToken = event["queryStringParameters"]["idToken"] 
    print(idToken)

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    payload = {
        "id_token": idToken,
        "client_id": "あなたのチャネルID",
    }

    res = requests.post(url, headers=headers, data=payload)

    print(json.dumps(res.json()))

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "API通信完了",
            # "location": ip.text.replace("\n", "")
        }),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        },
    }
