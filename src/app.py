import json
import requests
import boto3
import os
from decimal import Decimal

TABLE_NAME = os.environ.get('TABLE_NAME', 'AwsClickerCountryCounts')
table = boto3.resource('dynamodb').Table(TABLE_NAME)

# Custom encoder for converting Decimal types in DynamoDB responses to int
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    # Log event into CloudWatch
    print("Received event:", json.dumps(event, indent=2))

    country = "UNKNOWN"

    # Extract source IP
    source_ip = event.get('requestContext', {}).get('http', {}).get('sourceIp', 'UNKNOWN')

    # Determine the country based on the source IP
    if source_ip != "UNKNOWN":
        country = determine_country_from_ip(source_ip)

    # Increment the country in DynamoDB
    increment_country_count(country)

    # Return the updated country count

def determine_country_from_ip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        response.raise_for_status()

        data = response.json()
        return data.get("country", "UNKNOWN")

    except Exception as e:
        print(f"Error determining country for IP {ip}: {e}")
        return "UNKNOWN"
    
def increment_country_count(country):
    # Increment the press count for the country
    response = table.update_item(
        Key={'country': country},
        UpdateExpression="ADD press_count :incr",
        ExpressionAttributeNames={"#count": "press_count"},
        ExpressionAttributeValues={":incr": 1},
        ReturnValues="UPDATED_NEW"
    )

    # Log the updated press count
    print(f"Updated press count for {country}: {response['Attributes']['press_count']}")