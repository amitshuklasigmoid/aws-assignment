import json
import boto3
import datetime

def lambda_handler(event, context):
    data = json.loads(event['body'])
    
    bucket = 'amit1616' 
    s3 = boto3.client('s3')
    
    file_name = 'testdata' + str(datetime.datetime.now()) + '.json'
    
    uploadByteStream = bytes(json.dumps(data).encode('UTF-8'))
    
    s3.put_object(Bucket=bucket, Key=file_name, Body=uploadByteStream)
    
    response = {}
    response['filename'] = file_name 
    response['status_code'] = 200  
    return response  
