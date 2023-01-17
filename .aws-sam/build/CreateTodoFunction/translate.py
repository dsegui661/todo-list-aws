import json
import decimalencoder
import todoList
import boto3

def translate(event, context):
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])
    if item:
        
        #Translate item
        sourceLanguage = 'es'
        targetLanguage = event['pathParameters']['lang']
        
        translate = boto3.client(service_name='translate', use_ssl=True)
        result = translate.translate_text(Text=item, SourceLanguageCode=sourceLanguage, TargetLanguageCode=targetLanguage)
        
        #End item translate
        
        response = {
            "statusCode": 200,
            "body": json.dumps(result,
                               cls=decimalencoder.DecimalEncoder)
        }
    else:
        response = {
            "statusCode": 404,
            "body": ""
        }
    return response
