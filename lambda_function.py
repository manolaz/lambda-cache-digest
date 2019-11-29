import json
from redis import  Redis

def lambda_handler(event, context):
    """Entry Point for Lambda"""
    print("Received event: " + json.dumps(event, indent=2))
    try:
        r = Redis(host='i')
        key = event.get('key')
        print("KEY = {}".format(key))
        response = r.hgetall('user')
        print("CONTENT TYPE: " + response['ContentType'])
        print("CONTENT: " + response)
        return response
    except Exception as e:
        print(e)
        raise e
    return True