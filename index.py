import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'params': event.get('multiValueQueryStringParameters', {}),
        'path': event.get('path', {}),
        'stage': event.get('stage', {})
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
