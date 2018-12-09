import site
site.addsitedir('./packages')

import json
import datetime
import boto3
import os

def handler(event, context):
    params = event.get('multiValueQueryStringParameters', {})
    path = event.get('path', '').strip('/')
    stage = event.get('stage', {})
    stageVariables = event.get('stageVariables', {})
    httpMethod = event.get('httpMethod', '')
    
    if httpMethod == 'POST':
        body = event.get('body', '')
    else:
        body = ''
    
    action = ''
    if path == '':
        if httpMethod == 'GET':
            action = 'GET/'
        elif httpMethod == 'POST':
            action = 'POST/'
    elif path == 'preview':
        if httpMethod == 'GET':
            action = 'GET/preview'
    
    
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'params': params,
        'path': path,
        'stage': stage,
        'stageVariables': stageVariables,
        'httpMethod': httpMethod,
        'body': body,
        'action': action,
        'env': os.environ
    }
    
    
    
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
