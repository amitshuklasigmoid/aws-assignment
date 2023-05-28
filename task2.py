import boto3
import json
from datetime import datetime


def lambda_handler(event, context):

    BUCKET_NAME = 'amit1616'
    current_time = str(datetime.now())


    data = {'transaction_id': 12345, 'payment_mode': "card/netbanking/upi", 'amount': 200.0,"customer_id":101,"timestamp":current_time}

    s3_client = boto3.client('s3')

    file_name = current_time+'.json'
    json_data=json.dumps(data)

    s3_client.put_object(Body=json_data, Bucket=BUCKET_NAME, Key=file_name)
