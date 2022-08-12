import json
import saxo
import saxo_openapi as API

def handleRequest(event, context):
    client = API(access_token=os.getenv('AccessToken'))
    
    # Check valid request invoked
    if "request" in event["body"]:
        body = json.loads(event["body"])  
        request = body["request"].lower()
        if request == "view my positions":
            return {
                'statusCode': 200,
                'body': request
            } 
        elif request == "create an order":
            return {
                'statusCode': 200,
                'body': request
            }
        elif request == 'view my orders':
            return {
                'statusCode': 200,
                'body': request
            }
        elif request == 'create a price alert':
            return {
                'statusCode': 200,
                'body': request
            }
        elif request == 'view my price alerts':
            return {
                'statusCode': 200,
                'body': request
            }
        else:
            return {
                'statusCode': 200,
                'body': "Unknown Request"
            }
    else:
        return {
            'statusCode': 200,
            'body': 'Invalid Request'
        }
    # body = json.loads(event["body"])
    # return {
    #     'statusCode': 200,
    #     'body': body["request"]
    # }