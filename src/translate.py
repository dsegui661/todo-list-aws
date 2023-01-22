import json
import decimalencoder
import todoList
import boto3


def translate(event, context):
    # create a response
    item = todoList.get_item(event['pathParameters']['id'])
    if item:
        sourceLanguage = 'es'
        targetLanguage = event['pathParameters']['lang']
        print('TargetLanguage --> ' + targetLanguage)
        print('item --> ' + item)
        trans = boto3.client(service_name='translate', region_name='us-east-1',
                             use_ssl=True)
        result = trans.translate_text(Text=item,
                                      SourceLanguageCode=sourceLanguage,
                                      TargetLanguageCode=targetLanguage)
        print('TranslatedText: ' + result.get('TranslatedText'))
        print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
        print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))
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
