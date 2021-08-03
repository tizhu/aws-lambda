import json

def lambda_handler(event, context):
    # TODO implement 
    # make a change
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
