import json
import datetime
import PIL

def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'params': event.get('multiValueQueryStringParameters', {}),
        'PIL': PIL.VERSION
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
