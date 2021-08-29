import json, base64, gzip

def lambda_handler(event, context):
    message = event['awslogs']['data']

    compressed_payload = base64.b64decode(message)
    uncompressed_payload = gzip.decompress(compressed_payload)
    payload = json.loads(uncompressed_payload)

    msg = payload['logEvents'][0]['message']
    msg = json.loads(msg)
    dresp = msg['delivery']['providerResponse']

    ## Build the if-else logic here
    if dresp == 'No quota left for account':
        print (dresp)
        print ('Review your quota')
    else:
        print(dresp)

    return 'ok'
