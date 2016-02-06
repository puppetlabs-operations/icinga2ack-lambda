from __future__ import print_function
import requests
print('Loading function')

def lambda_handler(event, context):
    with open('./config.json') as f:
        config = json.loads(f.read())
    print("Received event: " + json.dumps(event, indent=2))
    for message in event['messages']:
        if message['type'] == 'incident.acknowledge':
            print("Oh boy!")
