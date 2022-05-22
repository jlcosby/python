#delete dynamodb table

import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('TableName')

table.delete()
