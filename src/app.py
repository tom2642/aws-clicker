import json
import requests
import boto3
import os
from decimal import Decimal

# Environment variables
TABLE_NAME = os.environ['TABLE_NAME']
DOMAIN_NAME = os.environ.get('DOMAIN_NAME')

# DynamoDB configuration
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

    # Get the HTTP method from the event object
    http_method = event.get('httpMethod')

    # Handle POST requests to increment country count
    if http_method == 'POST':
        country = "UNKNOWN"

        # Extract source IP and determine the country based on the source IP
        source_ip = event.get('requestContext', {}).get('identity', {}).get('sourceIp', 'UNKNOWN')
        if source_ip != "UNKNOWN":
            country = determine_country_from_ip(source_ip)

        # Increment the country in DynamoDB
        increment_country_count(country)

    # Fetch lastest country counts from DynamoDB
    all_country_counts = table.scan().get('Items', [])

    # Sort countries by click_count in descending order
    all_country_counts.sort(key=lambda item: item.get('click_count', 0), reverse=True)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': f'https://{DOMAIN_NAME}',
            'Access-Control-Allow-Methods': 'POST,GET'
        },
        'body': json.dumps(all_country_counts, cls=DecimalEncoder)
    }

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
    # Increment the click count for the country
    response = table.update_item(
        Key={'country': country},
        UpdateExpression="ADD click_count :incr",
        ExpressionAttributeValues={":incr": 1},
        ReturnValues="UPDATED_NEW"
    )

    # Log the updated click count
    print(f"Updated click count for {country}: {response['Attributes']['click_count']}")