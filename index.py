import site
site.addsitedir('./packages')

import json
import datetime
import boto3
import os

def handler(event, context):
    params = event.get('multiValueQueryStringParameters', {})
    path = event.get('path', '').strip('/')
    stage = context.get('stage', None)
    stageVariables = event.get('stageVariables', {})
    httpMethod = event.get('httpMethod', None)
    
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
        #'stage': str(stage,
        'event': str(event),
        'context': str(context),
        'stageVariables': stageVariables,
        'httpMethod': httpMethod,
        'body': body,
        'action': action,
        'env': str(os.environ)
    }
    
    
    
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
